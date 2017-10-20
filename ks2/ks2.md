# Kubernetes series part 2

The objective here is to try to obtain the same development experience as `yarn start` but using kubernetes.

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
    eval $(docker-machine env -u)
    ```

1. define CHOKIDAR_USEPOLLING in app folder

    create a `.env` inside the `app` folder with the following values:

    ```bash
    CHOKIDAR_USEPOLLING=true
    ```

    resources:

    * [ReactJs development on docker container](https://stackoverflow.com/questions/42976296/reactjs-development-on-docker-container/43065210#43065210)
    * [npm start doesn’t detect changes](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#npm-start-doesnt-detect-changes)

    > If the project runs inside a virtual machine such as (a Vagrant provisioned) VirtualBox, create an .env file in your project directory if it doesn’t exist, and add `CHOKIDAR_USEPOLLING=true` to it. This ensures that the next time you run npm start, the watcher uses the polling mode, as necessary inside a VM.

1. create docker image

    ```bash
    docker build -f ./web/Dockerfile -t ks2webimage .
    ```

1. mount frontend source code

    In a _separate_ terminal, in the root of the project (this terminal needs to keep running the **whole** time you're debugging...).

    ```bash
    ➜ minikube mount ./app/src:/mounted-ks2-app-src
    Mounting ./app/src into /mounted-ks2-app-src on the minikube VM
    This daemon process needs to stay alive for the mount to still be accessible...
    ufs starting
    ```

    For more information about mounting volumes read these [docs](https://github.com/kubernetes/minikube/blob/master/docs/host_folder_mount.md)

1. reference volume in deployment file

    Define your new volume next to images in the deployment file.

    ```yaml
    - name: frontend
      hostPath:
        path: /mounted-ks2-app-src/app/src
    ```

    And reference the new volume in the `ks2web` image

    ```yaml
    volumeMounts:
      - mountPath: /app/src
        name: frontend
    ```

1. create deployment and service

    ```bash
    ➜ kubectl create -f ./config/dev.ks.deployment.yaml
    deployment "ks2web" created

    ➜ kubectl create -f ./config/dev.ks.service.yaml
    service "ks2web" created
    ```

1. check cluster status

    ```bash
    ➜ kubectl get pods -w
      NAME                      READY     STATUS    RESTARTS   AGE
      ks2web-2024024258-2fc0t   1/1       Running   0          10s
    ```

    The `-w` stands for _watch_, so that you can see the different status changes of the pods.

1. service app

    Get URL and navigate to it.

    ```bash
    minikube service ks2web --url
    ```

1. verify that hot reload works.

    Make a change to app.js and notice the app reloads with latest code.

## Issues detecting changes

If variable `CHOKIDAR_USEPOLLING=true` is not set

I notice you get a looping crash in the app pod.

```bash
➜ kubectl get pods -w
NAME                      READY     STATUS    RESTARTS   AGE
ks2web-2517779699-mqwpm   0/1       Error     1          11s
ks2web-2517779699-mqwpm   0/1       CrashLoopBackOff   1         18s
ks2web-2517779699-mqwpm   1/1       Running   2         19s
ks2web-2517779699-mqwpm   0/1       Error     2         20s
ks2web-2517779699-mqwpm   0/1       CrashLoopBackOff   2         35s
```

```bash
➜ kubectl logs ks2web-2517779699-zh64c
yarn run v1.1.0
$ react-scripts start
Could not find a required file.
  Name: index.js
  Searched in: /app/src
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
```
