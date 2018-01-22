'ks7 config'

class Config(object):
    'base class for application configuration details.'
    SECRET_KEY = 'ks7'

    @staticmethod
    def init_app(app):
        'init app'
        pass
class DevelopmentConfig(Config):
    'dev config'
    DEBUG = True
    SERVE_STATIC_FILES = False
    MODE = 'development'


class TestingConfig(Config):
    'test config'
    DEBUG = False
    SERVE_STATIC_FILES = True
    MODE = 'production'

config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'default': TestingConfig
}
