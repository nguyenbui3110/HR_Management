import os
from dotenv import load_dotenv
from datetime import timedelta
load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES")))
JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES")))