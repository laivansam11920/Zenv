from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    # 1. APP CONFIG
    DEBUG: bool = Field(default=False, alias="DEBUG")
    SECRET_KEY: str = Field(..., alias="SECRET_KEY")

    # 2. FLASK CONFIG
    SESSION_COOKIE_SAMESITE: str = "Lax"
    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SECURE: bool = False

    # 3. MONGODB CONFIG
    MONGO_URI: str = Field(..., alias="MONGO_URI")
    MONGO_DB: str = Field(default="Zenv", alias="MONGO_DB")

    # 4. PYDANTIC CONFIG
    model_config = SettingsConfigDict(populate_by_name=True)

    def model_post_init(self, __context):
        self.SESSION_COOKIE_SECURE = not self.DEBUG


Configs = Settings()
