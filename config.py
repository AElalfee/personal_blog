import os
import secrets

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    DEBUG = os.getenv("DEBUG", "True") == "True"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
