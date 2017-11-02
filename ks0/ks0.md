# Why Docker and Kubernetes

Containers and containerized software allows us to build, ship and run distributed applications. It removes the machine contraints from applications. It also let us to create a complex application in a deterministic fashion.

Composing applications with containers in mind looks to make development, QA and production environments closer to each other and by doing so, changes can be shipped faster and testing a full system happens sooner.

[Docker](https://www.docker.com/what-docker) - the containerization platform - addresses these points, making software _independent_ of cloud providers.

Containers are not the full story as even with them the amount of work needed for shipping your application through any cloud provider (or in a private cloud) is significant. A normal application will need auto scaling groups, persistent remote discs, auto discovery, etc. Each cloud infrastructure provides different mechanisms for doing this. If you go down that path you very quickly become cloud platform dependent.

This is where [Kubernetes](https://kubernetes.io/) comes to play. It is an orchestration system for docker containers that allows you to manage containers, scaling and deploying different pieces of your application - in a standardized way - with great tooling as part of it. It's a portable abstraction that's compatible with the main cloud providers (Google Cloud, Amazon Web Services and Microsoft Azure all have support for it).

Also, it makes it easier for you and your team to have environments from development to production that are similar to each other. Something that previously required lots of time and effort is just provided by using Kubernetes.

The fact that you could start your application in your machine with the same pieces as in production closes the gaps between a development and a production environment. This makes developpers more aware of how an application is structures together even though they are only responsible for one piece of it. It also makes your application be fully tested earlier in the pipeline.

With this change arriving _slowly_ to the industry new questions arise; how should I develop against this clustered based environment? If we suppose you have 3 environments - development, QA and production - Docker containers and Kubernetes already take us very close in terms of environment similarity.

That said, differences across these environments will still exist, either in terms of development cycle (eg. time spent to see my code changed in the application I am running) or in terms of data (eg. I should probably not test with production data in my QA environment as it has sensitive information).

So, should I try to always work inside a Kubernetes cluster, build images, recreate deployments and services while I code? Or maybe I should not try too hard to make my development environment be a Kubernetes cluster(s) in development? Or maybe I should work in a hybrid way?

We've built this series of posts as we experiment with different ways to write software. As we do, we've tried to constrain ourselves to try and use Kubernetesin all environments so that we can explore the impact these technologies will have on the development and management of data and the database.

The series starts with the basic creation of a ReactJS application hooked up to Kubernetes, and elvolves to encompass more of our development requirements. By the end we'll have covered all of our application development needs _and_ understood how best to cater for the database lifecyce in this world of containers.

Is this a silver bullet? Probably not. We've tried to expose volumes and have a fast development cycle on the main places where code would change but this does not solve all problems and we encounter ourselves with slow development cycles in some places.
