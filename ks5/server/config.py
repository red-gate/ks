'ks5 config'
import logging

class Config(object):
    '''
    Base class for application configuration details.
    '''
    SECRET_KEY = 'ks.'

    @staticmethod
    def init_app(app):
        'init app'
        app.config['LOGGING_LEVEL'] = logging.DEBUG if app.config['DEBUG'] else logging.INFO
        app.config['MODE'] = 'production' if app.config['PROD'] else 'development'

class DevelopmentConfig(Config):
    'dev config'
    DEBUG = True
    PROD = False

class TestingConfig(Config):
    'test config'
    DEBUG = False
    PROD = True

config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'default': TestingConfig
}
