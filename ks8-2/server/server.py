'ks8-2 web server'

import logging
from os import getenv
from os.path import exists

import config

from flask import Flask
from flask import send_from_directory

import controllers.hello as controller_hello
import controllers.todo as controller_todo

app = Flask(__name__, static_folder='./app/build/static/')
app.logger.setLevel(logging.DEBUG)
config_name = getenv('FLASK_CONFIG', 'default')

if not config_name in config.config:
    raise ValueError('Invalid FLASK_CONFIG "{}", choose one of {}'.format(
        config_name,
        str.join(', ', config.config.keys())))

app.config.from_object(config.config[config_name])
config.config[config_name].init_app(app)

app.add_url_rule('/api/hello', view_func=controller_hello.hello, methods=['GET'])
app.add_url_rule('/api/todo/list', view_func=controller_todo.list_items, methods=['GET'])
app.add_url_rule('/api/todo/add', view_func=controller_todo.add, methods=['POST'])
app.add_url_rule('/api/todo/delete', view_func=controller_todo.delete, methods=['POST'])
app.add_url_rule('/api/todo/item/update', view_func=controller_todo.item_update, methods=['POST'])

def serve_static_paths(current_app):
    'serve static paths if in production mode'

    current_app.logger.info('setting prod static paths')
    if not current_app.config['SERVE_STATIC_FILES']:
        current_app.logger.info('skipping serving static files based on config')
        return
    current_app.logger.info('serving up static files')
    @current_app.route('/', defaults={'path': ''})
    @current_app.route('/<path:path>')
    def serve(path):
        'serve static files'
        if path == '':
            return send_from_directory('./app/build/', 'index.html')
        if exists('./app/build/' + path):
            return send_from_directory('./app/build/', path)
        return send_from_directory('./app/build/', 'index.html')

    current_app.logger.info('all ready, static paths set')

def log_config(current_app):
    'log current app config'
    current_app.logger.info('logging current config')
    current_app.logger.info('server is running in %s mode', current_app.config['MODE'])
    current_app.logger.info('config name "%s"', config_name)
    current_app.logger.info('current config keys: %s', str.join(', ', current_app.config.keys()))

serve_static_paths(app)
log_config(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
