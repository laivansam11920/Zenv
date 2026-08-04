from flask import Blueprint

get_env_bp: Blueprint = Blueprint('get_env', __name__)
login_bp: Blueprint = Blueprint('login', __name__)

@get_env_bp.post('/')
def get_env_route(): ...

@login_bp.post('/login')
def login_route(): ...