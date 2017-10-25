#!/bin/bash

command=${1:-create}

webImage=ks5webimage
webServerImage=ks5webserverimage

if [ $command = "dev" ]; then

    echo 'creating images...'
    docker build -f ./web/Dockerfile -t $webImage .
    docker build -f ./server/Dockerfile -t $webServerImage .

    echo 'creating services and deployments...'

    kubectl create -f ./config/dev.ks.deployment.yaml
    kubectl create -f ./config/dev.ks.service.yaml
    exit 0
fi

if [ $command = "test" ]; then

    echo 'creating images...'
    docker build -f ./server/Dockerfile -t $webServerImage .

    echo 'creating services and deployments...'

    kubectl create -f ./config/test.ks.deployment.yaml
    kubectl create -f ./config/test.ks.service.yaml
    exit 0
fi