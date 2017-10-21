# Kubernetes series part 3

The objective here is to ...

1. navigate to ks3

    ```bash
    ➜ pwd
        ~/dev/github/santiaago/ks/ks3
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

1. mount frontend source code

    In a _separate_ terminal, in the root of the project (this terminal needs to keep running the **whole** time you're debugging...).

    ```bash
    ➜ pwd
        ~/dev/github/santiaago/ks/ks3
    ➜ minikube mount ./app/src:/mounted-ks3-app-src
        Mounting ./app/src into /mounted-ks3-app-src on the minikube VM
        This daemon process needs to stay alive for the mount to still be accessible...
        ufs starting
    ```

    For more information about mounting volumes read these [docs](https://github.com/kubernetes/minikube/blob/master/docs/host_folder_mount.md)
