# Simulating the ZAp with Pub/Sub

Objetivo: Enviar e receber mensagens usando o modelo Pub/Sub com um broker RabbitMQ, simulando o funcionamento de um WhatsApp. O publish irá enviar mensagens de para o tópico da pessoa que deseja enviar e o consumer iŕa realizar uma subscription no topic com o nome dele, para receber as mensagens que são enviadas para pessoa.

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
