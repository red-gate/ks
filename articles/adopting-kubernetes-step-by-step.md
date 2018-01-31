Adopting Kubernetes step by step
===

**Note:** Original article is available on medium:
[Adopting Kubernetes step by step](https://medium.com/ingeniouslysimple/adopting-kubernetes-step-by-step-f93093c13dfe)

## Why Docker and Kubernetes

Containers allow us to build, ship and run distributed applications. They remove the machine constraints from applications and lets us create a complex application in a deterministic fashion.

Composing applications with containers allows us to make development, QA and production environments closer to each other (if you put the effort in to get there). By doing so, changes can be shipped faster and testing a full system can happen sooner.

Docker — the containerization platform — provides this, making software independent of cloud providers.

However, even with containers the amount of work needed for shipping your application through any cloud provider (or in a private cloud) is significant. An application usually needs auto scaling groups, persistent remote discs, auto discovery, etc. But each cloud provider has different mechanisms for doing this. If you want to support these features, you very quickly become cloud provider dependent.

This is where Kubernetes comes in to play. It is an orchestration system for containers that allows you to manage, scale and deploy different pieces of your application — in a standardised way — with great tooling as part of it. It’s a portable abstraction that’s compatible with the main cloud providers (Google Cloud, Amazon Web Services and Microsoft Azure all have support for Kubernetes).

A way to visualise your application, containers and Kubernetes is to think about your application as a shark — stay with me — that exists in the ocean (in this example, the ocean is your machine). The ocean may have other precious things you don’t want your shark to interact with, like clown fish. So you move you shark (your application) into a sealed aquarium (Container). This is great but not very robust. Your aquarium can break or maybe you want to build a tunnel to another aquarium where other fish live. Or maybe you want many copies of that aquarium in case one needs cleaning or maintenance… this is where Kubernetes clusters come to play.

Evolution to Kubernetes

With Kubernetes being supported by the main cloud providers, it makes it easier for you and your team to have environments from development to production that are almost identical to each other. This is because Kubernetes has no reliance on proprietary software, services or infrastructure.

The fact that you can start your application in your machine with the same pieces as in production closes the gaps between a development and a production environment. This makes developers more aware of how an application is structured together even though they might only be responsible for one piece of it. It also makes it easier for your application to be fully tested earlier in the pipeline.

## How do you work with Kubernetes?

With more people adopting Kubernetes new questions arise; how should I develop against a cluster based environment? Suppose you have 3 environments — development, QA and production — how do I fit Kubernetes in them? Differences across these environments will still exist, either in terms of development cycle (e.g. time spent to see my code changes in the application I’m running) or in terms of data (e.g. I probably shouldn’t test with production data in my QA environment as it has sensitive information).

So, should I always try to work inside a Kubernetes cluster, building images, recreating deployments and services while I code? Or maybe I should not try too hard to make my development environment be a Kubernetes cluster (or set of clusters) in development? Or maybe I should work in a hybrid way?

Development with a local cluster

If we carry on with our metaphor, the holes on the side represent a way to make changes to our app while keeping it in a development cluster. This is usually achieved via volumes.

## A Kubernetes series

The Kubernetes series repository is open source and available here:

## https://github.com/red-gate/ks

We’ve written this series as we experiment with different ways to build software. We’ve tried to constrain ourselves to use Kubernetes in all environments so that we can explore the impact these technologies will have on the development and management of data and the database.

The series starts with the basic creation of a React application hooked up to Kubernetes, and evolves to encompass more of our development requirements. By the end we’ll have covered all of our application development needs and have understood how best to cater for the database lifecycle in this world of containers and clusters.

Here are the first 5 episodes of this series:

* ks1: build a React app with Kubernetes
* ks2: make minikube detect React code changes
* ks3: add a python web server that hosts an API
* ks4: make minikube detect Python code changes
* ks5: create a test environment

The second part of the series will add a database and try to work out the best way to evolve our application alongside it.

By running Kubernetes in all environments, we’ve been forced to solve new problems as we try to keep the development cycle as fast as possible. The trade-off being that we are constantly exposed to Kubernetes and become more accustomed to it. By doing so, development teams become responsible for production environments, which is no longer difficult as all environments (development through production) are all managed in the same way.

## What’s next?

We will continue this series by incorporating a database and experimenting to find the best way to have a seamless database lifecycle experience with Kubernetes.

_This Kubernetes series is brought to you by Foundry, Redgate’s R&D division. We’re working on making it easier to manage data alongside containerised environments, so if you’re working with data and containerised environments, we’d like to hear from you — reach out directly to the development team at foundry@red-gate.com_
