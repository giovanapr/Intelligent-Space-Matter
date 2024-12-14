# Send and Consume Messages

Objective: Send and receive images using the Pub/Sub model with a RabbitMQ broker.

### Broker

```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Publish

```
docker run -it --rm -v <local_directory>:/app/<container_directory> --network <network_mode> giovanapr/pub-img:v1
```
Example:
```
docker run -it --rm -v /testes_cursoIS/Trabalho-IS/Trabalho-Send-Images:/app/images --network host giovanapr/pub-img:v1
```

### Consumer

```
docker run -it --network host giovanapr/sub-zap:v3
```
