#!/bin/bash

command=${1:-create}

webImage=ks5webimage
webServerImage=ks5webserverimage

haswebimage(){ docker images | grep $webImage | wc -l;}
haswebserverimage(){ docker images | grep $webServerImage | wc -l;}


if [ $command = "dev" ]; then
    echo 'removing services and deployments...'

    kubectl delete -f ./config/dev.ks.service.yaml
    kubectl delete -f ./config/dev.ks.deployment.yaml

    echo 'removing images...'

    isready=`haswebserverimage`
    echo need to delete webServerImage $(( $isready > 1 ))
    while (($isready>0))
    do
        echo trying to remove $webServerImage
        {
            docker rmi $webServerImage
        } || {
            isready=`haswebserverimage`
            echo need to delete $webServerImage $isready
            sleep 7
        }
    done

    isready=`haswebimage`
    echo need to delete webImage $(( $isready>1 ))
    while (($isready>0))
    do
        echo trying to remove $webImage
        {
            docker rmi $webImage
         } || {
            isready=`haswebimage`
            echo need to delete $webServerImage $isready
            sleep 7
         }
    done
    echo dev environment deleted
    exit 0

fi

if [ $command = "test" ]; then
    echo 'removing services and deployments...'

    kubectl delete -f ./config/test.ks.deployment.yaml
    kubectl delete -f ./config/test.ks.service.yaml
    
    echo 'removing images...'

    isready=`haswebserverimage`
    echo need to delete webServerImage $(( $isready > 1 ))
    while (($isready>0))
    do
        echo trying to remove $webServerImage
        {
            docker rmi $webServerImage
        } || {
            isready=`haswebserverimage`
            echo need to delete webServerImage $isready
            sleep 7
        }
    done

    echo test environment deleted
    exit 0
fi
