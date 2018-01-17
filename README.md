# ks

A Kubernetes series

Docker, Kubernetes + the database.

Here we showcase the evolution of a simple web application as we learn Docker and Kubernetes. Our only contraint is to try use Kubernetes through all our environments while we evolve the application from a development enviroment to a production environment and add different pieces as we go.

## Why Kubernetes

To deploy, scale and manage containerized applications.

* [Why containers](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/#why-containers)
* [Why do I need Kubernetes and what can it do?](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/#why-do-i-need-kubernetes-and-what-can-it-do)
* [4 reasons you should use Kubernetes](https://www.infoworld.com/article/3173266/containers/4-reasons-you-should-use-kubernetes.html)

## Prerequisites

* [Yarn](https://yarnpkg.com/lang/en/docs/install/)
* [Docker](https://www.docker.com/get-docker)
* Kubernetes:
  * Follow this [tutorial](https://kubernetes.io/docs/tutorials/stateless-application/hello-minikube/) to set up kubernetes in your machine.

## Structure of this repo

* Each `ksx` folder (`ks1`, `ks2`, ...) contains a working example of the app we are building in this series.
* They are all incremental, so `ksn` is based on `ksn-1`, etc..
* instructions of each item of this series is in the `ksx.md` file.

## Getting started

1. clone ks repo
    ```bash
    git clone https://github.com/red-gate/ks.git
    ```

1. start following the series or go directly to the one you are interested in.

## Evolution of our app

[ks0: an introduction to our ks series](./ks0/ks0.md)

1. [ks1: build a React app with kubernetes](./ks1/ks1.md)
1. [ks2: make minikube detect React code changes](./ks2/ks2.md)
1. [ks3: add a python web server that hosts an API](./ks3/ks3.md)
1. [ks4: make minikube detect Python code changes](./ks4/ks4.md)
1. [ks5: use helm to deploy the application](./ks5/ks5.md)
1. [ks6: create a test environment using helm](./ks6/ks6.md)
1. ...
1. create a prod environment
