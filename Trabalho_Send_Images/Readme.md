# Trabalho Enviar e Consumir Imagens

Objetivo: Enviar e receber imagens usando o modelo Pub/Sub com um broker RabbitMQ.

### Broker

```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Publish

```
docker run -it --rm -v <local_directory>:/app/<container_directory> --network <network_mode> giovanapr/pub-img:v1
```

### Consumer

```
docker run -it --network host giovanapr/sub-zap:v3
```
