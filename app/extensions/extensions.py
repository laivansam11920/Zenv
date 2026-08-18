from flask_login import LoginManager
from argon2 import PasswordHasher

__all__ = ["login_manager", "ph"]

login_manager: LoginManager = LoginManager()
ph: PasswordHasher = PasswordHasher()
