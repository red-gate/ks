'ks5 config'
import logging

class Config(object):
    'base class for application configuration details.'
    SECRET_KEY = 'ks5'

    @staticmethod
    def init_app(app):
        'init app'
        pass
class DevelopmentConfig(Config):
    'dev config'
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG
    SERVE_STATIC_FILES = True
    MODE = 'development'


class TestingConfig(Config):
    'test config'
    DEBUG = False
    LOGGING_LEVEL = logging.INFO
    SERVE_STATIC_FILES = True
    MODE = 'production'

config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'default': TestingConfig
}
