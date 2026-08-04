from flask import Flask, render_template
from configs import Configs
from app.routes import register_routes

def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = Configs.SECRET_KEY
    app.config.from_object(Configs)
    register_routes(app)
    @app.route("/")
    def index():
        return render_template("index.html")

    return app
