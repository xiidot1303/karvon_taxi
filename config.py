import os
from dotenv import load_dotenv

load_dotenv(os.path.join(".env"))

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

# Postgres db informations
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

# Telegram bot tokens
BOT_API_TOKEN = os.environ.get("BOT_API_TOKEN")

# Yandex
YANDEX_CLIENT_ID = os.environ.get("YANDEX_CLIENT_ID")
YANDEX_API_KEY = os.environ.get("YANDEX_API_KEY")

# Click
CLICK_SERVICE_ID = os.environ.get("CLICK_SERVICE_ID")