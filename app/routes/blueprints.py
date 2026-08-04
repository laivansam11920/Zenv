from .routes import *

def register_routes(app):
    app.register_blueprint(get_env)