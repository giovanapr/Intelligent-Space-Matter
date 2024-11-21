from __future__ import print_function
from is_wire.core import Channel, Subscription, Logger
import time

log = Logger(name='Giovana')

log.info("Indicate the broker's IP and port")
IP = input(f"IP (or ENTER for localhost): ") or "localhost"
PORT = input(f"PORT (or ENTER for 5672): ") or "5672"

log.info("Broker login")
user = input(f"Username (or ENTER for guest): ") or "guest"
password = input(f"Password (or ENTER for guest): ") or "guest"

#Connect to the broker
channel = Channel(f"amqp://{user}:{password}@{IP}:{PORT}")
log.info(f"Created channel - amqp://{user}:{password}@{IP}:{PORT}")

log.info("----------------Receive messages------------------")

#Subscribe to the desired topic(s)
subscription = Subscription(channel)
subscription.subscribe(topic='Aluno.Giovana')

while True:
    message = channel.consume()

    print(f"{message.reply_to}: {message.body.decode('latin1')}")

    time.sleep(1)
