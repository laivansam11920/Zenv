from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username: str, /, password: str, user_id: str, role: str="user", last_update: str=""):
        self.username: str = username
        self.password: str = password
        self.id: str = user_id
        self.role: str = role
        self.last_update: str = last_update

    @property
    def get_id(self) -> str:
        return self.id

    @property
    def get_username(self) -> str:
        return self.username

    @staticmethod
    def get(user_id: str) -> User | None:
        from app.database import db

        user: dict = db.user.find_one(
            { "user_id": user_id },
            { "_id": 0, "username": 1, "password": 1, "role": 1 }
        )

        if not user:
            return None

        return User(
            str(user.get("username", "")),
            password=str(user.get("password", "")),
            user_id=str(user.get("user_id", "")),
            role=str(user.get("role", "user")),
            last_update=str(user.get("last_update", "")),
        )
