'todo list controller'
import json
from flask import request

from flask import jsonify
from flask import current_app

import data.database as database

def list_items():
    'GET todo list'
    current_app.logger.info('todo controller called, func: list')
    db = database.Database(current_app.config['CONN_STRING'])
    items = db.get_items()
    return jsonify({
        'todoList': items
    })

def add():
    'POST add item into todo list'
    current_app.logger.info('todo controller called, func: add')

    data = json.loads(request.data.decode("utf-8"))
    item = data['newItem']

    db = database.Database(current_app.config['CONN_STRING'])
    db.insert_item(item)
    items = db.get_items()

    return jsonify({
        'todoList': items
    })

def delete():
    'POST delete item from list'
    current_app.logger.info('todo controller called, func: delete')

    data = json.loads(request.data.decode("utf-8"))
    item = data['itemToDelete']

    db = database.Database(current_app.config['CONN_STRING'])
    db.delete_item(item)
    items = db.get_items()

    return jsonify({
        'todoList': items
    })

def item_update():
    'POST update item in list'
    current_app.logger.info('todo controller called, func: item_update')

    data = json.loads(request.data.decode('utf-8'))
    item = data['itemToUpdate']

    db = database.Database(current_app.config['CONN_STRING'])
    db.update_item(item)
    items = db.get_items()

    return jsonify({
        'todoList': items
    })
