# Docker run

>docker run hello-world         Most basic use of a Docker image is to run it and let it exist

* Azure
>docker run -it mcr.microsoft.com/azure-cli
>docker run -it -v ${HOME}/.ssh:/root/.ssh mcr.microsoft.com/azure-cli       pick up your SSH keys


* MYSQL
Create two MySql Containers (each command as one line)
>docker run -p 3310:3306 --name=mysql1 -e MYSQL_ROOT_PASSWORD=pw -d mysql:5.6              -d: run the container in detached mode (in the background)
>docker run -p 3311:3306 --name=mysql2 -e MYSQL_ROOT_PASSWORD=pw -d mysql:5.6
>docker container exec -it mysql1 /bin/sh      start in interactive mode: you can use cli
mysql -p pw
select * from ...
>docker container exec -it mysql2 /bin/sh
[application-layer sharding with shard key](https://itnext.io/how-to-use-database-sharding-and-scale-an-asp-net-core-microservice-architecture-22c24916590f)

https://hub.docker.com/_/Mysql

>docker run --name some-mysql -v /my/own/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
-v mounts the /my/own/datadir directory from the underlying host system as /var/lib/mysql inside the container, where MySQL by default will write its data files.

Database dumps
>docker exec some-mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /some/path/on/your/host/all-databases.sql

Restoring data from dump files
>docker exec -i some-mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < /some/path/on/your/host/all-databases.sql


* RABBITMQ
Start a RabbitMQ container with admin UI 
>docker run -d  -p 15672:15672 -p 5672:5672 --hostname my-rabbit --name some-rabbit rabbitmq:3-management
Browse localhost:15672 
Log in with the username/password guest/guest
Use the web UI to create an Exchange with the name “user” of type “Fanout” and two queues “user.postservice” and “user.otherservice”. It is important to use the type “Fanout” so that the exchange copies the message to all connected queues.
