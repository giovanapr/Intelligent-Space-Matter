from is_wire.core import Channel, Subscription, Message, Logger
from is_msgs.image_pb2 import Image
import numpy as np
import cv2
import json
import time

log = Logger(name='Consumer')

def to_np(input_image):
    if isinstance(input_image, np.ndarray):
        output_image = input_image
    elif isinstance(input_image, Image):
        buffer = np.frombuffer(input_image.data, dtype=np.uint8)
        output_image = cv2.imdecode(buffer, flags=cv2.IMREAD_COLOR)
    else:
        output_image = np.array([], dtype=np.uint8)
    return output_image

log.info("Indicate the broker's IP and port")
IP = input(f"IP (or ENTER for localhost): ") or "localhost"
PORT = input(f"PORT (or ENTER for 5672): ") or "5672"

log.info("Broker login")
user = input(f"Username (or ENTER for guest): ") or "guest"
password = input(f"Password (or ENTER for guest): ") or "guest"

#Connect to the broker
channel = Channel(f"amqp://{user}:{password}@{IP}:{PORT}")
log.info(f"Created channel - amqp://{user}:{password}@{IP}:{PORT}")

if __name__ == '__main__':

    subscription = Subscription(channel)
    subscription.subscribe(topic="Topic.Frame")

    while True:
      log.info("Waiting for Images")
      msg = channel.consume()
      img_unpack = msg.unpack(Image)
      imgNP = to_np(img_unpack)

      filename = '/data/image_rcvd.jpg' #Directory to save to volume

      cv2.imwrite(filename, imgNP)
      log.info("Image saved")
