import os
from dotenv import load_dotenv

load_dotenv()

APP_SWAGGER_URL = os.environ.get("APP_SWAGGER_URL", default=None)
APP_REDOC_URL = os.environ.get("APP_REDOC_URL", default=None)
APP_HOST = os.environ.get("APP_HOST", default="0.0.0.0")
APP_PORT = int(os.environ.get("APP_PORT", default=8000))
