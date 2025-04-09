from flask import Flask, request, jsonify, render_template
import random
import os
from dotenv import load_dotenv
import requests

# 設置 Flask 應用
app = Flask(__name__)

# 加載環境變數
load_dotenv()

# 配置 Mailgun API
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")  # 從 .env 文件加載 API 密鑰
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")    # 從 .env 文件加載自定義域名
MAILGUN_API_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"

# 驗證碼字典（在實際部署中，你可能會使用 Redis 或資料庫來儲存）
captcha_codes = {}

# 首頁路由
@app.route('/')
def index():
    return render_template('register.html')

# 驗證 email 並發送驗證碼
@app.route('/api/verify-email', methods=['POST'])
def verify_email():
    email = request.json.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    # 隨機生成驗證碼
    captcha_code = str(random.randint(100000, 999999))

    # 發送驗證碼到 email
    try:
        send_email(email, '您的驗證碼', f'請輸入此驗證碼來完成註冊：{captcha_code}')
        captcha_codes[email] = captcha_code  # 儲存 email 和驗證碼
        return jsonify({"message": "Verification code sent to your email"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 發送電子郵件的函數（使用 Mailgun）
def send_email(to_email, subject, body):
    data = {
        "from": f"Excited User <postmaster@{MAILGUN_DOMAIN}>",  # 發送者的地址
        "to": to_email,
        "subject": subject,
        "text": body
    }

    response = requests.post(
        MAILGUN_API_URL,
        auth=("api", MAILGUN_API_KEY),
        data=data
    )

    if response.status_code == 200:
        print(f"Email sent successfully to {to_email}")
    else:
        print(f"Failed to send email. Status code: {response.status_code}")
        print(response.text)
        raise Exception(f"Failed to send email: {response.text}")

# 驗證驗證碼是否正確
@app.route('/api/verify-captcha', methods=['POST'])
def verify_captcha():
    email = request.json.get('email')
    captcha = request.json.get('captcha')

    if not email or not captcha:
        return jsonify({"error": "Email and captcha are required"}), 400

    # 檢查 email 是否存在於驗證碼字典中
    if email not in captcha_codes:
        return jsonify({"error": "Email not found or not verified"}), 404

    # 檢查驗證碼是否正確
    if captcha_codes[email] == captcha:
        return jsonify({"message": "Captcha verified successfully"}), 200
    else:
        return jsonify({"error": "Invalid captcha"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5002)