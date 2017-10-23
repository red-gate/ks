# Kubernetes series part 4

The objective here is to update our app so that we can detect python code changes on the fly.
This will speed up development cycles.

1. navigate to ks4

    ```bash
    ➜ pwd
        ~/dev/github/santiaago/ks/ks4
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

1. build web docker image

    ```bash
    ➜ docker build -f ./web/Dockerfile -t ks4webimage .
    ```

1. build web server docker image

    ```bash
    ➜ docker build -f ./server/Dockerfile -t ks4webserverimage .
    ```

1. mount frontend source code

    In a _separate_ terminal, in the root of the project (this terminal needs to keep running the **whole** time you're debugging...).

    ```bash
    ➜ pwd
        ~/dev/github/santiaago/ks/ks4
    ➜ minikube mount .:/mounted-ks3-app-src
        Mounting ./app/src into /mounted-ks3-app-src on the minikube VM
        This daemon process needs to stay alive for the mount to still be accessible...
        ufs starting
    ```

    For more information about mounting volumes read these [docs](https://github.com/kubernetes/minikube/blob/master/docs/host_folder_mount.md)

1. create deployment and service

    ```bash
    ➜ kubectl create -f ./config/dev.ks.deployment.yaml
        deployment "ks4web" created

    ➜ kubectl create -f ./config/dev.ks.service.yaml
        service "ks4web" created
    ➜ kubectl get all
        NAME            DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
        deploy/ks4web   1         1         1            1           1m

        NAME                   DESIRED   CURRENT   READY     AGE
        rs/ks4web-1748674206   1         1         1         1m

        NAME            DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
        deploy/ks4web   1         1         1            1           1m

        NAME                         READY     STATUS    RESTARTS   AGE
        po/ks4web-1748674206-g14vb   2/2       Running   0          1m
    ```

1. get web server logs

    ```bash
    ➜ kubectl logs ks4web-1748674206-g14vb ks4webserver
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        * Restarting with stat
        /usr/local/lib/python3.5/runpy.py:125: RuntimeWarning: 'flask.cli' found in sys.modules after import of package 'flask', but prior to execution of 'flask.cli'; this may result in unpredictable behaviour
        warn(RuntimeWarning(msg))
        * Debugger is active!
        * Debugger PIN: 207-014-748
    ```

1. navigate to `./app`

    ```bash
    ➜ minikube service ks4web
    ```

1. we can now call the web server from our frontend code

    * we add a proxy to the `./app/package.json` file to `http://localhost:5000`
        `"proxy": "http://localhost:5000"`
    * add fetch api to frontend
        `yarn add whatwg-fetch`

1. delete deployment and docker image

    changes to the package.json are not taken into account when yarn start is running.
    To do that you will have to delete your deployment and recreate your docker image.

    ```bash
    ➜ kubectl delete -f ./config/dev.ks.deployment.yaml
    ➜ docker rmi ks4webimage
    ```

    Then recreate image and deployment.

    ```bash
    ➜ docker build -f ./web/Dockerfile -t ks4webimage .
    ➜ kubectl create -f ./config/dev.ks.deployment.yaml
    ```

1. check app runs as expected

    ```bash
    ➜ kubectl get pods
    ```

1. service app with minikube

    ```bash
    ➜ minikube service ks4web --url
    ```