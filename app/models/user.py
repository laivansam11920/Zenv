from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class UserInfo:
    email: str
    password: str
    user_id: str | None
    role: str = "user"
    last_update: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")