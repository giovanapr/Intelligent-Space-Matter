# Simulating the ZAp with Pub/Sub

Objective: Send and receive messages using the Pub/Sub model with a RabbitMQ broker, simulating the functionality of WhatsApp. The publisher will send messages to the topic of the intended recipient, and the consumer will subscribe to their own topic to receive messages sent to them.

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
