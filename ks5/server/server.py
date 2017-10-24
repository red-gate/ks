'ks5 web server'

from os import getenv
from os.path import exists

import config

from flask import Flask
from flask import send_from_directory

import controllers.hello as controller_hello

app = Flask(__name__, static_folder='./app/build/static/')

CONFIG_NAME = getenv('FLASK_CONFIG', 'default')

app.config.from_object(config.config[CONFIG_NAME])
config.config[CONFIG_NAME].init_app(app)

app.logger.setLevel(app.config['LOGGING_LEVEL'])

app.add_url_rule('/api/hello', view_func=controller_hello.hello, methods=['GET'])

if __name__ == '__main__':
    app.logger.info('starting server in %s mode', app.config['MODE'])

    if app.config['PROD']:
        app.logger.info('setting prod static paths')
        @app.route('/', defaults={'path': ''})
        @app.route('/<path:path>')
        def serve(path):
            'serve static files'
            if path == '':
                return send_from_directory('./app/build/', 'index.html')
            app.logger.info('looking for :%s', ('./app/build/' + path))
            if exists('./app/build/' + path):
                return send_from_directory('./app/build/', path)
            return send_from_directory('./app/build/', 'index.html')

    app.logger.info('all ready, starting server')
    app.run(host='0.0.0.0', port=5000)
