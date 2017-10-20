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

1. let mounting volume you need polling mechanism

create a `.env` inside the `app` folder with the following values:

```bash
CHOKIDAR_USEPOLLING=true
```

1. create docker image

```bash
docker build -f ./web/Dockerfile -t ks2webimage .
```

1. mount frontend source code

In a _separate_ terminal, in the root of the project (this terminal needs to keep running the **whole** time you're debugging...).

```bash
➜ minikube mount ./app/src:/mounted-ks2-app-src
Mounting ./app/src into /k8s-mounted-app-ks2 on the minikube VM
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

1. service app

    Get URL and navigate to it.

    ```bash
    minikube service ks2web --url
    ```

1. verify that hot reload works.

  Make a change to app.js and notice the app reloads with latest code.

## issues

1. if variable `CHOKIDAR_USEPOLLING=true` is not set

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
