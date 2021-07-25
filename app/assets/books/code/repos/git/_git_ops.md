# Git ops

Git + ops

- https://www.gitops.tech/

everything is (or should be) defined as code Stored in Git (the source of truth)

Defining everything as code, storing that code in Git, and letting the machines detect the drift between the desired and the actual state – and making sure that drifts are resolved as soon as possible, hence resulting in the two states being almost always in sync.

“If DevOps is a way of life, GitOps is prescriptive about how you practice it"
“Store everything in Git”
“You store your code and infrastructure and build configuration information in your Git repository”

a way of implementing Continuous Deployment for cloud native applications. It focuses on a developer-centric experience when operating infrastructure, by using tools developers are already familiar with, including Git and Continuous Deployment tools.

The core idea of GitOps is having a Git repository that always contains declarative descriptions of the infrastructure currently desired in the production environment and an automated process to make the production environment match the described state in the repository. If you want to deploy a new application or update an existing one, you only need to update the repository - the automated process handles everything else. It’s like having cruise control for managing your applications in production.

GitOps: versioned CI/CD on top of declarative infrastructure. Stop scripting and start shipping.

GitOps is not limited to Kubernetes. In principle, you can use any infrastructure that can be observed and described declaratively, and has Infrastructure as Code tools available. However, currently most operators for pull-based GitOps are implemented with Kubernetes in mind.

## What is GitOps?
“GitOps is a prescriptive, controlled way of practicing DevOps unified around a single repository of artifacts for all actors involved across the development and operations teams in the software development lifecycle”

“GitOps consists of a set of automation practices and tools that enables effective management of infrastructure and continuous deployment for cloud native applications.”

“GitOps is a pattern, where a source control system (like Git) is used as a reliable source of information about infrastructure and any changes can be applied just after a pull-request (classic pipeline for Git). GitOps is a pattern for Infrastructure as Code used to control, maintain and manage any resources (preferably cloud resources) and collect information about infrastructure, services, applications and deployments. Also, GitOps as a separate practice may well be a part of a set of DevOps practices, and it is aimed at closer interactions with developers.”

“GitOps is the acknowledgement that everything is (or should be) defined as code. With all code in Git, Git becomes the source of truth (or, to be a little more precise, the desired state of the whole system). If Git is the source of truth, you cannot run operations manually by executing random commands. Doing so would mean that Git would stop being the only source of truth. Instead, the only goal of humans (operations) is to define the desired state as code and store it in Git. Then, let the machines synchronize that with the actual state. Such synchronization must be continuous so that the two states are (almost) always in sync. In other words, GitOps is about defining everything as code, storing that code in Git, and letting the machines detect the drift between the desired and the actual state – and making sure that drifts are resolved as soon as possible, hence resulting in the two states being almost always in sync.”

## Tools

- https://itnext.io/kubernetes-essential-tools-2021-def12e84c572
- https://www.gitops.tech/

ArgoCD: A GitOps operator for Kubernetes with a web interface
Flux: The GitOps Kubernetes operator by the creators of GitOps — Weaveworks
Gitkube: A tool for building and deploying docker images on Kubernetes using git push
JenkinsX: Continuous Delivery on Kubernetes with built-in GitOps
Terragrunt: A wrapper for Terraform for keeping configurations DRY, and managing remote state
WKSctl: A tool for Kubernetes cluster configuration management based on GitOps principles
Helm Operator: An operator for using GitOps on K8s with Helm
werf: A CLI tool to build images and deploy them to Kubernetes via push-based approach

## more
- https://www.gitops.tech/
- https://enterprisersproject.com/article/2021/6/gitops-explained-plain-english
- https://www.youtube.com/watch?v=f5EpcWp0THw&t=459s

xs code project: Separate repo for infrastructure as code project + full devops pipeline for it
