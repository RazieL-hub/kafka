import os
from functools import lru_cache

from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER_EMAIL = os.path.join(BASE_DIR, 'templates')

# CREDENTIALS for EMAIL
conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_PORT=int(os.getenv('MAIL_PORT')),
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_FROM=os.getenv('MAIL_FROM'),
    MAIL_FROM_NAME=os.getenv('MAIL_FROM_NAME'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    TEMPLATE_FOLDER=TEMPLATE_FOLDER_EMAIL
)

# CREDENTIALS for TELEGRAM
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
