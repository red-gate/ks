# Kubernetes series part 7

The objective here is to modify our backend and frontend code so that we can have a Todo application that stores things in memory.

1. start minikube and build docker images

```bash
➜ cd ks7
➜ minikube start
➜ eval $(minikube docker-env)
➜ docker build -f ./server/Dockerfile -t ks7webserverimage .
➜ docker build -f ./web/Dockerfile -t ks7webimage .
```

1. mount volume

```bash
➜ cd ks7
➜ minikube mount .:/mounted-ks7-src
```

1. install helm chart

```bash
➜ helm install ./ks -n ks
```

1. check app is working properly

```bash
➜ kubectl get pods
NAME                         READY     STATUS    RESTARTS   AGE
ks-ks7web-7444588647-j8tmb   2/2       Running   0          30s
```

1. check logs

```bash
➜ kubectl logs ks-ks7web-7444588647-j8tmb ks7webfrontend
➜ kubectl logs ks-ks7web-7444588647-j8tmb ks7webserver
```

1. test app in browser

```bash
➜ minikube service ks-ks7web-service
```