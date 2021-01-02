# KUBERNETES (K8s) 

https://kubernetes.io/

open-source orchestration tool for automation: deployment, management and monitoring of containerized applications, workloads and services. All cloud providers are offering their own branded versions of Kubernetes, including Google, Microsoft, Amazon

- kubernetes master
    API server that communicates with kubelets to ensure that packages are running as it should. 
- Kubelet 
    Primary node agent that runs on a node. It is responsible for the state of each node, ensuring that all containers on the node are up and running.

open-source system for automation used to manage containerized workloads and services. All cloud providers are offering their own branded versions of Kubernetes, including Google, Microsoft, Amazon

### Package management

download.md(assets/slides/cloud/pm_helm.md)

### Kubernetes Applications

*Stateless applications
trivial to scale, with no coordination. These can take advantage of Kubernetes deployments directly and work great behind Kubernetes Services or Ingress Services.

* Stateful applications
postgres, mysql, etc which generally exist as single processes and persist to disks. These systems generally should be pinned to a single machine and use a single Kubernetes persistent disk. These systems can be served by static configuration of pods, persistent disks, etc or utilize StatefulSets.

* Static distributed applications
zookeeper, cassandra, etc which are hard to reconfigure at runtime but do replicate data around for data safety. These systems have configuration files that are hard to update consistently and are well-served by StatefulSets.

* Clustered applications
etcd, redis, prometheus, vitess, rethinkdb, etc are built for dynamic reconfiguration and modern infrastructure where things are often changing. They have APIs to reconfigure members in the cluster and just need glue to be operated natively seemlessly on Kubernetes, and thus the Kubernetes Operator concept

### Kubernetes vs OpenStack
Openstack was launched in 2010. AWS was the only Cloud, GCP didn't exist, Docker was not a thing. The goal was to provide an open source and private alternative to AWS; building on top of VMs.

Kubernetees was launched in 2014. AWS, Azure, GCP became dominant players of Cloud computing, Docker became the synonym of container. The goal was to be a bridge among the big 3, and between public cloud and private data centers; building on top of containers.

OpenStack is dying down. Kubernetes is the winner, for now.