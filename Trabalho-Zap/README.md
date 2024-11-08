# Trabalho ZAP

Objetivo: Enviar e receber mensagens usando o modelo Pub/Sub com um broker RabbitMQ.

### Broker

```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Publish

```
docker run -it --network host giovanapr/pub-zap:v4
```

### Consumer

```
docker run -it --network host giovanapr/sub-zap:v3
```
