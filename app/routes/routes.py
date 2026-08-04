from flask import Blueprint

get_env: Blueprint = Blueprint('get_env', __name__)

@get_env.post('/')
def get_env_route(): ...