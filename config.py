class Config:
    SERVER_NAME = '127.0.0.1:8080'
    SECRET_KEY = '123456789'
    DEBUG = True
    TESTING = False
    TEMPLATE_FOLDER = 'views/templates'
    STATIC_FOLDER = 'views/static'

class DevelopmentConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = True