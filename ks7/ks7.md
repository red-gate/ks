# Kubernetes series part 7

The objective here is to modify our backend and frontend code so that we can have a Todo application that stores things in memory.

```bash
minikube start
eval $(minikube docker-env)
docker build -f ./server/Dockerfile -t ks7webserverimage .
docker build -f ./web/Dockerfile -t ks7webimage .
```

```bash
minikube mount .:/mounted-ks7-src
```

```bash
helm install ./ks -n ks
```

