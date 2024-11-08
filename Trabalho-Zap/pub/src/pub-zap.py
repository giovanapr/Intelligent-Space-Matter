from is_wire.core import Channel, Message, Logger

log = Logger(name='Matheus')

log.info("Indicate the broker's IP and port")
IP = input(f"IP (or ENTER for localhost): ") or "localhost"
PORT = input(f"PORT (or ENTER for 5672): ") or "5672"

log.info("Broker login")
user = input(f"Username (or ENTER for guest): ") or "guest"
password = input(f"Password (or ENTER for guest): ") or "guest"

#Connect to the broker
channel = Channel(f"amqp://{user}:{password}@{IP}:{PORT}")
log.info(f"Created channel - amqp://{user}:{password}@{IP}:{PORT}")

message = Message()

log.info("----------------Send Messages------------------")

destination = ""

while True:
    if destination == "":
        destination = input(f"For: ")
    else:
        # Salve destination name
        destination = input(f"For (or use Enter for {destination}): ") or destination

    # Message that will be sent
    message.body = input('Message: ').encode('latin1')

    # Declares who is sending the message
    message.reply_to = "Matheus"

    # Publish message
    channel.publish(message, topic=f"Aluno.{destination}")
    log.info(f"Message sent to {destination}")
