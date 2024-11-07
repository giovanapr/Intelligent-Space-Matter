from is_wire.core import Channel, Message, Logger

log = Logger(name='Matheus')

#Connect to the broker
channel = Channel("amqp://guest:guest@10.10.0.120:5672")

message = Message()

log.info("----------------Send Messages------------------")

last_destination = "none"

while True:
    # Salve destination name
    destination = input(f"For (or use Enter for {last_destination}): ") or last_destination

    # Message that will be sent
    message.body = input('Message: ').encode('latin1')

    # Declares who is sending the message
    message.reply_to = "Matheus"

    # Save the last destination
    last_destination = destination

    # Publish message
    channel.publish(message, topic=f"Aluno.{destination}")
