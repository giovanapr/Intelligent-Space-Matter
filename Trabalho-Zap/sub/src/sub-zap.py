from __future__ import print_function
from is_wire.core import Channel, Subscription, Logger
import time

log = Logger(name='Giovana')

#Connect to the broker
channel = Channel("amqp://guest:guest@10.10.0.120:5672")

log.info("----------------Receive messages------------------")

#Subscribe to the desired topic(s)
subscription = Subscription(channel)
subscription.subscribe(topic='Aluno.Giovana')

while True:
    message = channel.consume()

    print(f"{message.reply_to}: {message.body.decode('latin1')}")

    time.sleep(1)
