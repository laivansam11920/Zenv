from flask import Blueprint
from app.controllers.auth.login import LoginController

get_env_bp: Blueprint = Blueprint('get_env_bp', __name__)
save_env_bp = Blueprint('save_env_bp', __name__)
login_bp: Blueprint = Blueprint('login_bp', __name__)

@get_env_bp.get('/get_env')
def get_env_route(): ...

@save_env_bp.post('/save_env')
def save_env_route(): ...

@login_bp.post('/login')
def login_route() -> LoginController: ...