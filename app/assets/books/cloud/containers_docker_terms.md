# Docker Terms

* DOCKER IMAGE
a template containing instructions to create containers
The file system and configuration of our application which are used to create containers. To find out more about a Docker image, run docker inspect alpine. In the demo above, you used the docker pull command to download the alpine image. When you executed the command docker run hello-world, it also did a docker pull behind the scenes to download the hello-world image. Read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization.

A package with all the dependencies and information needed to create a container. An image includes all the dependencies (such as frameworks) plus deployment and execution configuration to be used by a container runtime. Usually, an image derives from multiple base images that are layers stacked on top of each other to form the container’s filesystem. An image is immutable once it has been created.

* DOCKER CONTAINER
A Container is the running instance of an image
Running instances of Docker images — containers run the actual applications. A container includes an application and all of its dependencies. It shares the kernel with other containers, and runs as an isolated process in user space on the host OS. You created a container using docker run which you did using the alpine image that you downloaded. A list of running containers can be seen using the docker ps command.

An instance of a Docker image. A container represents the execution of a single application, process, or service. It consists of the contents of a Docker image, an execution environment, and a standard set of instructions. When scaling a service, you create multiple instances of a container from the same image. Or a batch job can create multiple containers from the same image, passing different parameters to each instance.


* DOCKER DAEMON
The background service running on the host that manages building, running and distributing Docker containers.
The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. ⚠️ A daemon can also communicate with other daemons to manage Docker services.
>docker run -i -t ubuntu /bin/bash
  runs an ubuntu container
  attaches interactively to your local command-line session
  runs /bin/bash
If you do not have the ubuntu image locally, Docker pulls it from your configured registry, as though you had run docker pull ubuntu manually.

* DOCKER CLIENT - The command line tool that allows the user to interact with the Docker daemon.

* DOCKER STORE - A registry of Docker images, where you can find trusted and enterprise ready containers, plugins, and Docker editions. You'll be using this later in this tutorial.



* DOCKERFILE
A text file that contains instructions for building a Docker image. It’s like a batch script, the first line states the base image to begin with and then follow the instructions to install required programs, copy files, and so on, until you get the working environment you need.

* BUILD
The action of building a container image based on the information and context provided by its Dockerfile, plus additional files in the folder where the image is built. You can build images with the following Docker command:
docker build

* VOLUMES
Offer a writable filesystem that the container can use. Since images are read-only but most programs need to write to the filesystem, volumes add a writable layer, on top of the container image, so the programs have access to a writable filesystem. The program doesn’t know it’s accessing a layered filesystem, it’s just the filesystem as usual. Volumes live in the host system and are managed by Docker.

* TAG
A mark or label you can apply to images so that different images or versions of the same image (depending on the version number or the target environment) can be identified.

* MULTI-STAGE BUILD
Is a feature, since Docker 17.05 or higher, that helps to reduce the size of the final images. In a few sentences, with multi-stage build you can use, for example, a large base image, containing the SDK, for compiling and publishing the application and then using the publishing folder with a small runtime-only base image, to produce a much smaller final image.

* REPOSITORY (REPO)
A collection of related Docker images, labeled with a tag that indicates the image version. Some repos contain multiple variants of a specific image, such as an image containing SDKs (heavier), an image containing only runtimes (lighter), etc. Those variants can be marked with tags. A single repo can contain platform variants, such as a Linux image and a Windows image.

* REGISTRY
A service that provides access to repositories. The default registry for most public images is Docker Hub (owned by Docker as an organization). A registry usually contains repositories from multiple teams. Companies often have private registries to store and manage images they’ve created. Azure Container Registry is another example.


* DOCKER HUB
A public registry to upload images and work with them. Docker Hub provides Docker image hosting, public or private registries, build triggers and web hooks, and integration with GitHub and Bitbucket.

* AZURE CONTAINER REGISTRY
A public resource for working with Docker images and its components in Azure. This provides a registry that’s close to your deployments in Azure and that gives you control over access, making it possible to use your Azure Active Directory groups and permissions.

* DOCKER TRUSTED REGISTRY (DTR)
A Docker registry service (from Docker) that can be installed on-premises so it lives within the organization’s datacenter and network. It’s convenient for private images that should be managed within the enterprise. Docker Trusted Registry is included as part of the Docker Datacenter product. For more information, see Docker Trusted Registry (DTR).



* MULTI-ARCH IMAGE
For multi-architecture, it’s a feature that simplifies the selection of the appropriate image, according to the platform where Docker is running. For example, when a Dockerfile requests a base image mcr.microsoft.com/dotnet/sdk:5.0 from the registry, it actually gets 5.0-nanoserver-1909, 5.0-nanoserver-1809 or 5.0-buster-slim, depending on the operating system and version where Docker is running.

* DOCKER COMMUNITY EDITION (CE)
Development tools for Windows and macOS for building, running, and testing containers locally. Docker CE for Windows provides development environments for both Linux and Windows Containers. The Linux Docker host on Windows is based on a Hyper-V virtual machine. The host for Windows Containers is directly based on Windows. Docker CE for Mac is based on the Apple Hypervisor framework and the xhyve hypervisor, which provides a Linux Docker host virtual machine on macOS X. Docker CE for Windows and for Mac replaces Docker Toolbox, which was based on Oracle VirtualBox.

* DOCKER ENTERPRISE EDITION (EE)
An enterprise-scale version of Docker tools for Linux and Windows development.

* COMPOSE
A command-line tool and YAML file format with metadata for defining and running multi-container applications. You define a single application based on multiple images with one or more .yml files that can override values depending on the environment. After you’ve created the definitions, you can deploy the whole multi-container application with a single command (docker-compose up) that creates a container per image on the Docker host.

* CLUSTER
A collection of Docker hosts exposed as if it were a single virtual Docker host, so that the application can scale to multiple instances of the services spread across multiple hosts within the cluster. Docker clusters can be created with Kubernetes, Azure Service Fabric, Docker Swarm and Mesosphere DC/OS.

* ORCHESTRATOR
A tool that simplifies management of clusters and Docker hosts. 
Orchestrators enable you to manage their images, containers, and hosts through a command-line interface (CLI) or a graphical UI. You can manage container networking, configurations, load balancing, service discovery, high availability, Docker host configuration, and more. An orchestrator is responsible for running, distributing, scaling, and healing workloads across a collection of nodes. Typically, orchestrator products are the same products that provide cluster infrastructure, like Kubernetes and Azure Service Fabric, among other offerings in the market