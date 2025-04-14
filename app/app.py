from flask import Flask, render_template
from app.routers.auth import auth_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
