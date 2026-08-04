from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

from .configs import Configs

__all__ = ["Configs"]
