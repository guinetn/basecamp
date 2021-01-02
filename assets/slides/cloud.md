# Cloud

Systems (most distributed systems), with the hardware procurement and maintenance and many other things abstracted away from software developers.
Evolution: bare metal → virtualized → containerized → cloud → serverless

• Virtualisation
    The key enabler of the Cloud so that the resources can be split and re-packaged to sell: 
    virtual machine(hypervisor)
    virtualized (software-defined) storage and network

    Hyper-converged infrastructure (HCI): 
        software-defined infrastructure
        virtualizes all of the elements of conventional "hardware-defined" systems.
• Datacenter software-defined (SDDC)
• Architecture orientée service (SOA)
• Services Cloud
    Cloud offers dozens of services but there are 3 key categories:
    - COMPUTE: VM, containers, serverless functions…
    - STORAGE: databases, datawarehouses, object stores…
    - NETWORKING: DNS, VPC, load balancing…
• Cloud Types
    
    PUBLIC: your infrastructure is running by...
        - Amazon AWS
        - Microsoft Azure
        - Google Cloud Platform
        - Alibaba Cloud (China) 
        - Oracle
        - IBM

        [GCP vs AWS](https://cloud.google.com/docs/compare/aws#service_comparisons)
        [GCP vs Azure](https://cloud.google.com/docs/compare/azure#service_comparisons)
    
    PRIVATE: you own your data center but resource request and allocation is done through software UI
    
    HYBRID: taking the best parts of public and private cloud

----

## The Stack
* Servers (including bare metal, VMs, containers, serverless functions to run the applications and backends: AWS EC2 or GCP GCE
* Databases to store data and make them readily available for appliations, and indexes to speed up searches and filters.
* Caches to speed up reads by remembering results of expensive operations
* Data Warehouse to store historical data for analytics
* Storage to store files and objects (can also be used to serve static websites)
* Message queues to communicate between processes and enable async operations.
* Logging: AWS Kinesis, Fluentd, GCP Cloud Logging
* Monitoring to monitor system health and key business metrics, and send out alerts: GCP Cloud Monitoring, Datadog
* Service Discovery, Configs and Secrets: Consul/Vault
* Orchestration / Provision: Kubernetes, Terraform
* Package format: a common way to package all the applications, e.g. Docker
* Code management: git or hg
* CI/CD: continuous integration and deployment
----
download.md(assets/slides/cloud/edge_computing.md)
----
download.md(assets/slides/cloud/cloud_models.md)
----
download.md(assets/slides/cloud/infrastructure_as_code.md)
----
download.md(assets/slides/cloud/cloud_automation.md)
----
download.md(assets/slides/cloud/cloud_orchestration.md)
----
download.md(assets/slides/cloud/cloud_monitoring.md)
----
download.md(assets/slides/cloud/containers.md)
----
download.md(assets/slides/cloud/vm.md)
----
download.md(assets/slides/cloud/containers_docker.md)
----
download.md(assets/slides/cloud/containers_kubernetes.md)
----
download.md(assets/slides/cloud/containers_vagrant.md)
----
download.md(assets/slides/cloud/aws.md)
----
download.md(assets/slides/cloud/azure.md)
----
download.md(assets/slides/cloud/google_cloud.md)
----

