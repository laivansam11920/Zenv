from app.services.auth.login import Login
from app.utils.logger import logger
from flask import request
from app.models.auth import User
from app.models.user import UserInfo
from flask_login import login_user as login_user_lib

class LoginController:

    @staticmethod
    def login():

        if request.method == "POST":
            data = request.get_json() or request.form

            email = data.get("email")
            password = data.get("password")
            remember = data.get("remember") == True

            if not email or not password:
                return {"success": False, "message": "Email and password are required"}, 404

            if not Login.check(UserInfo(password=password, email=email, user_id=None)):
                return {"success": False, "message": "Incorrect username or password"}, 401

            load_user = User.get("user_id")

            if not load_user or not load_user.is_active():
                return {"success": False, "message": "This account is inactive"}, 403

            login_user_lib(load_user, remember=remember)

            return {"success": True, "message": "Login successful"}



