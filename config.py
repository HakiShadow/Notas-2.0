class Config:
    SERVER_NAME = 'localhost.localdomain:8080'
    SECRET_KEY = '123456789'
    DEBUG = False
    TESTING = False
    TEMPLATE_FOLDER = 'views/templates'
    STATIC_FOLDER = 'views/static'

class DevelopmentConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = True