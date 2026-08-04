from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, password, user_id):
        self.username: str = username
        self.password: str = password
        self.id: str = user_id

    @property
    def get_id(self) -> str:
        return self.id

    @property
    def get_username(self) -> str:
        return self.username

    @staticmethod
    def get(user_id: str) -> User | None:
        from app.database import db

        user = db.user.find_one({ "user_id": user_id }, { "_id": 0, "username": 1, "password": 1 })

        if not user:
            return None

        return User(user_id=user.get("user_id"), username=user.get("username"), password=user.get("password"))

