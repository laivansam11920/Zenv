from flask import Flask
from configs import Configs
from app.routes import register_routes
from app.extensions import login_manager


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(Configs)

    login_manager.init_app(app)

    login_manager.login_view = "login_route"
    login_manager.session_protection = "strong"

    import middlewares.auth_loader  # type: ignore

    register_routes(app)

    return app
