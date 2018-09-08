Title: Running App in Docker (1)
Date: 2018-09-08 19:30:00 +1200
Category: Container
Tags: docker, container, 
Slug: docker-run

## Docker Run

When you are likely to run a container on your own machine, you need two steps.

1. Find the image repository and a proper tag.
2. Use `docker run` to set container runtime parameters and then start.

### Example

We'd like to run a RabbitMQ on your local machine. First, we choose an image from the [official repository](https://hub.docker.com/_/rabbitmq/). E.g. we choose `rabbitmq:management-alpine`. So we got the basic command:
```bash
$ docker run rabbitmq:management-alpine
```

To add port forwarding to the container, we need to specify the `-p` parameter:

```bash
$ docker run \
-p 5672:5672 \
-p 15672:15672 \
rabbitmq:management-alpine
```

It replace our host port `5672` and `15672` with the container's.

After that, we'd like to give a reasonable name to the container and ask the container auto start after my docker daemon is restarted. So I need to add command `--name` and `--restart`:

```bash
$ docker run \
-p 5672:5672 \
-p 15672:15672 \
--name dev-rabbitmq \
--restart always \
-d \
rabbitmq:management-alpine
```

And don't forget the `-d` if you don't want to attach the container STDIN/STDOUT.