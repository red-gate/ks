# Introdution

Containers and containerized software allows us to build, ship and run distributed applications. It removes the machine contraints from applications. It also let us to create a complex application in a deterministic fashon.

Composing applications with containers in mind looks to make development, QA and production environments closer to eachother and by doing so shiping changes faster and testing a full system as early as posible.

[Docker](https://www.docker.com/what-docker) addresses these points making software _independent_ of cloud providers.

Containers are not the full story as even with them the amount of work needed for shipping your application through any cloud provider (or in a private cloud) is significant. A normal application will need auto scaling groups, persistent remote discs, auto discovery, etc. And each cloud infrastructure provides different mechanisms for doing this. If you go down that path you become very fast cloud platform dependent.

This is where [Kubernetes](https://kubernetes.io/) comes to play. It is an orchestration system for docker containers that allows you to manage containers, scaling and deploying different pieces of your application in a standard way, and with great tooling as part of it. It's a portable abstraction to work against as all cloud providers (AWS, Azure and Amazon support it).

Also, it makes it easier for you and your team to have environemnts from development to production that are similar to each other. Something that required lots of time and effort before is almost given to you by using kubernetes.

The fact that you could start your application in your machine with the same pieces as in production closes the gaps between a development and a production environment. This makes developpers more aware of how an application is structures together even though they are only responsible for one piece of it. It also makes your application be fully tested earlier in the pipeline.

With this changes arriving _slowly_ to the industry new questions arise. How should I develop against this clustered based environment. If we suppose you have 3 environments development, QA and production. Docker containers and Kubernetes already take us very close in terms of environment similarity.

We still need differences across these environments either in terms of development cycle (time spent to see my code changed in the application I am running) or in terms of data (I should probably not test with production data in my QA environment as it has sensitive information).

Should I try to always work inside a kubernetes cluster, build images, re create deployments and services while I code. Or maybe I should not try too hard to make my development environment be a kubernetes cluster(s) in development. Or maybe I should work in a hybrid way.

We built this series while we experiment different ways to write software while trying to constrain ourselves to always use our application through kubernetes.

Is this a silver bullet? probably not, we tried to expose volumes and have a fast development cycle on the main places where code would change but this does not solve all problems and we encounter ourselves with slow development cycles in some places.