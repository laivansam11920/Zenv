from flask import Flask, render_template
from configs import Configs

def create_app():
    app = Flask(__name__)
    app.secret_key = Configs.SECRET_KEY
    app.config.from_object(Configs)
    @app.route('/')
    def index():
        return render_template('index.html')

    return app