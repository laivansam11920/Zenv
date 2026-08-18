from app.database import db
from app.extensions import ph
from argon2.exceptions import VerifyMismatchError
from threading import Thread


class Login:

    @classmethod
    def check(cls, email: str, password: str) -> bool:
        user = db.users.find_one({"email": email}, {"_id": 0, "password": 1})

        if not user or "password" not in user:
            return False

        stored_hash: str = user["password"]

        try:
            ph.verify(hash=stored_hash, password=password)

            if ph.check_needs_rehash(stored_hash):
                Thread(
                    target=cls._update_password_hash,
                    args=(email, ph.hash(password)),
                    daemon=True,
                ).start()

            return True

        except (VerifyMismatchError, Exception, KeyError):
            return False

    @staticmethod
    def _update_password_hash(email: str, new_hash: str) -> None:
        db.users.update_one({"email": email}, {"$set": {"password": new_hash}})

