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
        'DATABASE_URI', default='postgresql://gofaniyi:gofaniyi@gofaniyi.cuawszxylysg.us-east-2.rds.amazonaws.com:5432/insurance')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False
    API_BASE_URL_V1 = getenv('API_BASE_URL_V1', default='/api/v1')

    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY', '\xfb*\xae\xef\xe6\xddn\x9e\xef\xad\xbc\xdf\xb4!;\xed2X\xe7?\x86\xc9\x91\x85')
    BCRYPT_LOG_ROUNDS = 4

    # FLASK_ENV Configuration
    FLASK_ENV = getenv('FLASK_ENV', 'development')

    FLASKS3_BUCKET_NAME= getenv('AWS_BUCKET', 'zappa-ok587zsna')

class ProductionConfig(Config):
    """App production configuration."""
    pass


class DevelopmentConfig(Config):
    """App development configuration."""
    DEBUG = False


class StagingConfig(Config):
    """App staging configuration."""
    pass


class TestingConfig(Config):
    """App testing configuration."""

    TESTING = True
    CELERY_ALWAYS_EAGER = True
    SQLALCHEMY_DATABASE_URI = getenv(
        'TEST_DATABASE_URI', default='postgresql://postgres:backend@localhost:5433/insurance_test')

    JWT_SECRET_KEY='\x95T\xe2\x8f\x8a\xa1a\xb0\x8d\x01\xd3\xea\x93X\xfb\x91ik\x9d\x96f\x83\xae\xab'
    FLASK_ENV = 'testing'


config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

AppConfig = TestingConfig if 'pytest' in sys.modules else config.get(
    getenv('FLASK_ENV'), 'development')
