'ks8-1 config'
import os

class Config(object):
    'base class for application configuration details.'
    SECRET_KEY = 'ks8-1'

    @staticmethod
    def init_app(app):
        'init app'
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_password = os.getenv('DB_PASSWORD')
        app.config['CONN_STRING'] = ("dbname='%s' user='%s' host='%s' port='%s' password='%s'" % 
                                     (db_name, db_user, db_host, db_port, db_password))

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
