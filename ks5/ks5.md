# Kubernetes series part 5

The objective here is to create a test environment - that is build the frontend and serve it in our python server as static resources.

To do this we will create a separate deployment and we will enhance our python server to take the environment into account.

This means we will not use volumes in our `test` environment, only in our `dev` environment.

1. navigate to ks5

    ```bash
    ➜ pwd
        ~/dev/github/santiaago/ks/ks5
    ```

1. start minikube

    ```bash
    ➜ minikube start
    ```

1. switch to minikube context

    ```bash
    ➜ eval $(minikube docker-env)
    ```

    If you ever need to switch back to your machine's context do:

    ```bash
    ➜ eval $(docker-machine env -u)
    ```

1. build frontend app

    ```bash
    ➜ cd app
    ➜ yarn
    ➜ yarn build
        yarn run v1.1.0
        $ react-scripts build
        Creating an optimized production build...
        Compiled successfully.

        File sizes after gzip:

        39.7 KB  build/static/js/main.2fba1481.js
        175 B    build/static/css/main.5fcf01d3.css

        ...
        The build folder is ready to be deployed.
        You may serve it with a static server:
        ...
        ✨  Done in 6.36s.
    ```

1. we update the web server to server our built app

    ```python
    'ks5 web server'

    import logging
    from os import getenv
    from os.path import exists

    import config

    from flask import Flask
    from flask import send_from_directory

    import controllers.hello as controller_hello

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

    def serve_static_paths(current_app):
        'configure static paths if in production mode'

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
            current_app.logger.warning('looking for :%s', ('./app/build/' + path))
            if exists('./app/build/' + path):
                return send_from_directory('./app/build/', path)
            return send_from_directory('./app/build/', 'index.html')

        current_app.logger.info('all ready, static paths set')

    serve_static_paths(app)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    ```

    This reference a `./server/config.py` config module.

    ```python
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
    ```

1. we update the webserver dockerfile

    To add the `app/build` folder when building the image.

    ```dockerfile
    WORKDIR ..

    ADD ./server ./server
    ADD ./app/build ./server/app/build

    WORKDIR /server
    ```

1. build web server docker image

    ```bash
    ➜ docker build -f ./server/Dockerfile -t ks5webserverimage .
    ```

1. we add a `test.ks.deployment.yaml` file for our test environment

    This deployment file only needs to reference the `webserver` as we no longer need a frontend image if we serve the react app from static files.

    We can remove the following:
    - the ks5web image section
    - the volumes sections
    - the python commands as we are not running in development

    We can add a `FLASK_CONFIG`

    ```yaml
    - name: FLASK_CONFIG
          value: "testing"
    ```

    ![test yaml diff ](./images/test.yaml.diff.png)

1. modify `dev.ks.deployment.yaml` file

    The development deployment config now needs the `FLASK_CONFIG` environment variable in order to load the development config.

    ```yaml
      - name: FLASK_CONFIG
        value: "dev"
    ```

1. create the test deployment and service

    ```bash
    ➜ kubectl create -f ./config/test.ks.deployment.yaml
        deployment "ks5web" created

    ➜ kubectl create -f ./config/test.ks.service.yaml
        service "ks5web" created
    ➜ kubectl get all
        NAME            DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
        deploy/ks5web   1         1         1            1           41s

        NAME                   DESIRED   CURRENT   READY     AGE
        rs/ks5web-2201989947   1         1         1         41s

        NAME            DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
        deploy/ks5web   1         1         1            1           41s

        NAME                         READY     STATUS    RESTARTS   AGE
        po/ks5web-2201989947-1b6sr   1/1       Running   0          41s
    ```

1. service ks5web

    ```bash
    ➜ minikube service ks5web --url
    ```

1. get web server logs

    ```bash
    ➜ kubectl logs ks5web-2201989947-1b6sr
         * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
        172.17.0.1 - - [25/Oct/2017 16:56:01] "GET / HTTP/1.1" 200 -
        172.17.0.1 - - [25/Oct/2017 16:56:01] "GET /static/css/main.5fcf01d3.css HTTP/1.1" 200 -
        172.17.0.1 - - [25/Oct/2017 16:56:01] "GET /static/js/main.2fba1481.js HTTP/1.1" 200 -
        172.17.0.1 - - [25/Oct/2017 16:56:01] "GET /static/css/main.5fcf01d3.css.map HTTP/1.1" 200 -
        172.17.0.1 - - [25/Oct/2017 16:56:01] "GET /api/hello HTTP/1.1" 200 -
        172.17.0.1 - - [25/Oct/2017 16:56:01] "GET /static/js/main.2fba1481.js.map HTTP/1.1" 200 -
    ```