from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    SECRET_KEY: str = Field(..., alias="SECRET_KEY")
    model_config = SettingsConfigDict(populate_by_name=True)
    DEBUG: bool = Field(default=False, alias="DEBUG")
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = DEBUG
    SESSION_COOKIE_HTTPONLY = True


Configs = Settings()