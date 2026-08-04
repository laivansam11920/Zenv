from flask import Blueprint, render_template
from app.controllers.auth.login import LoginController

get_env_bp: Blueprint = Blueprint("get_env_bp", __name__)
save_env_bp = Blueprint("save_env_bp", __name__)
login_bp: Blueprint = Blueprint("login_bp", __name__)
main: Blueprint = Blueprint("main_bp", __name__)


@main.route("/", methods=["GET", "POST", "DELETE", "PUT"])
def home():
    return render_template("index.html")


@get_env_bp.get("/get_env")
def get_env_route(): ...


@save_env_bp.post("/save_env")
def save_env_route(): ...


@login_bp.route("/login", methods=["GET", "POST"])
def login_route() -> LoginController: ...
