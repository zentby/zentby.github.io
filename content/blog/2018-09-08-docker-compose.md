Title: Running App in Docker (2)
Date: 2018-09-08 20:30:00 +1200
Category: Container
Tags: docker, container, 
Slug: docker-compose

## Docker Compose

`docker run` can be tedious sometimes if you have a lot of parameters to pass in or you need to re-run the container multiple times.

Docker Compose is a tool that can help you run the commands via the definition in a `yml` file. We call the `.yml` file as "docker-compose file".

>YAML is a human friendly data serialization standard for all programming languages.


### Example

Our example in [last post]({filename}./2018-09-08-docker-run.md) can fit into a "docker-compose" file:

```yml
version: '3'
services:
rabbit-mq:
image: rabbitmq:management-alpine
container_name: dev-rabbitmq
restart: always
ports:
- 15672:15672
- 5672:5672
```

You can always find a corresponding config in the file for your `docker run` command. Then you can start your RabbitMQ with a very few command.

```bash
$ docker-compose up -d
```

More complicated, we can build serveral services together into one "docker-compose" file:

```yml
version: '3'
services:
redis:
image: redis:alpine
container_name: dev-redis
restart: always
ports:
- 6379:6379
networks: 
- devnet

rabbit-mq:
image: rabbitmq:management-alpine
container_name: dev-rabbitmq
restart: always
ports:
- 15672:15672
- 5672:5672
networks:
- devnet

couch-db:
container_name: dev-couchdb
image: klaemo/couchdb:latest
restart: always
volumes:
- ./couchdb/local:/opt/couchdb/etc/local.d
- ./couchdb/data:/opt/couchdb/data
ports:
- 5984:5984
networks:
- devnet

networks:
devnet:
```

In the above docker-compose file, it also defines a "network" for the containers so that those containers are isolated from other containers.

Save the configs into a text file named `docker-compose.yml`. Then you can start all the containers together via the command:

```bash
$ docker-compose up --detach
```

It will auto load the `docker-compose.yml` file and start the containers for you. You can also use parameter `-f` to specify a docker-compose file:

```bash
$ docker-compose up \
-f docker-compose.yml \
-d
```
