import os
from pathlib import Path

class Config:
    """Base configuration"""
    BASE_DIR = Path(__file__).parent

    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{BASE_DIR / "instance" / "app.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Keygen.sh
    KEYGEN_ACCOUNT_ID = os.environ.get('KEYGEN_ACCOUNT_ID', '')
    KEYGEN_PRODUCT_ID = os.environ.get('KEYGEN_PRODUCT_ID', '')
    KEYGEN_API_TOKEN = os.environ.get('KEYGEN_API_TOKEN', '')
    KEYGEN_API_URL = 'https://api.keygen.sh/v1'

    # WhatsApp Business API
    WHATSAPP_API_TOKEN = os.environ.get('WHATSAPP_API_TOKEN', '')
    WHATSAPP_PHONE_NUMBER_ID = os.environ.get('WHATSAPP_PHONE_NUMBER_ID', '')
    WHATSAPP_API_URL = 'https://graph.facebook.com/v18.0'

    # Upload settings
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB max file size
    UPLOAD_FOLDER = BASE_DIR / 'uploads'
    ALLOWED_EXTENSIONS = {'xlsx', 'xls'}


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
