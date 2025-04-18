from flask import Flask, render_template
from app.routers.auth import auth_bp
from app.routers.activity import activity_bp
from app.routers.memeber import member_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp)
    app.register_blueprint(activity_bp)
    app.register_blueprint(member_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
