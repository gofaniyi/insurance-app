"""Application configuration module."""

import sys

from os import getenv
from pathlib import Path  # python3 only

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)


class Config(object):
    """App base configuration."""

    SQLALCHEMY_DATABASE_URI = getenv(
        'DATABASE_URI', default='postgresql://localhost/activo')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    API_BASE_URL_V1 = getenv('API_BASE_URL_V1')

    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
    BCRYPT_LOG_ROUNDS = 4


    # FLASK_ENV Configuration
    FLASK_ENV = getenv('FLASK_ENV')


class ProductionConfig(Config):
    """App production configuration."""
    pass


class DevelopmentConfig(Config):
    """App development configuration."""
    DEBUG = True


class StagingConfig(Config):
    """App staging configuration."""
    pass


class TestingConfig(Config):
    """App testing configuration."""

    TESTING = True
    CELERY_ALWAYS_EAGER = True
    SQLALCHEMY_DATABASE_URI = getenv(
        'TEST_DATABASE_URI', default='postgresql://localhost/activo_test')
    FLASK_ENV = 'testing'


config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

AppConfig = TestingConfig if 'pytest' in sys.modules else config.get(
    getenv('FLASK_ENV'), 'development')
