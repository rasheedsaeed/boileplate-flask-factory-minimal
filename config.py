import os
from dotenv import load_dotenv

# take environment variables from .env
load_dotenv()  

class Config:
    """
    Base configuration class.
    """

    # Default settings
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = False

    # Settings applicable to all environments
    SECRET_KEY = os.getenv("SECRET_KEY", default="A dubious key.")

    # Server config
    SERVER_NAME = "localhost:4001"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    FLASK_ENV = "production"
