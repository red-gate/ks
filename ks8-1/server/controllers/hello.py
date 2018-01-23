'hello controller'

from flask import jsonify
from flask import current_app

def hello():
    'GET hello'
    current_app.logger.info('hello controller called')
    return jsonify({
        'message': 'world'
    })
