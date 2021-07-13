## DOCKER COMPOSE

Tool for defining and running multi-container Docker applications. 
Compose use a YAML file to configure your application’s services.

A command-line tool and YAML file format with metadata for defining and running multi-container applications. You define a single application based on multiple images with one or more .yml files that can override values depending on the environment. After you’ve created the definitions, you can deploy the whole multi-container application with a single command (docker-compose up) that creates a container per image on the Docker host.

- https://docs.docker.com/compose/
- https://docs.docker.com/engine/
 
1. Dockerfile: Define your app’s environment so it can be reproduced anywhere.
2. docker-compose.yml: Define the services that make up your app so they can be run together in an isolated environment.
3. Run docker-compose up and Compose starts and runs your entire app.

Compose files 
- docker-compose.yml 
- docker-stack.yml