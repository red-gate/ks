'ks3 web server'

from flask import Flask

import controllers.hello as controller_hello

app = Flask(__name__)

app.add_url_rule('/api/hello', view_func=controller_hello.hello, methods=['GET'])

if __name__ == '__main__':
    app.logger.info('starting server in development mode')
    app.logger.info('all ready, starting server')
    app.run(host='0.0.0.0', port=5000)
