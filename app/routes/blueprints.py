from .routes import *
from flask import Flask

def register_routes(app: Flask):
    app.register_blueprint(get_env_bp)
    app.register_blueprint(login_bp)