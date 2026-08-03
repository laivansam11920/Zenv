from flask import Flask, render_template
from configs import Configs
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins="*") #<--
    app.secret_key = Configs.SECRET_KEY
    app.config.from_object(Configs)
    @app.route('/')
    def index():
        return render_template('index.html')

    return app