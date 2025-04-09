from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 替換成你自己的 MySQL 帳號密碼和資料庫名稱
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Aa221511%%40@127.0.0.1/sports_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# 測試資料庫連線
def test_database_connection():
    try:
        # 嘗試建立連線並執行簡單查詢
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            print("成功連線到資料庫!")
    except Exception as e:
        print("無法連線到資料庫:", e)

# 呼叫測試資料庫連線的函數
test_database_connection()