from flask import Blueprint

get_env = Blueprint('get_env', __name__)

@get_env.post('/')
def get_env(): ...