from is_wire.core import Channel, Subscription, Message, Logger
from is_msgs.image_pb2 import Image
import numpy as np
import cv2
import json
import time
import os

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

log.info("Loading environment variables...")
IP = os.getenv("IP", "localhost")
PORT = os.getenv("PORT", "5672")
topic = os.getenv("TOPIC", "image")

#Connect to the broker
channel = Channel(f"amqp://guest:guest@{IP}:{PORT}")
log.info(f"Created channel - amqp://guest:guest@{IP}:{PORT}")

if __name__ == '__main__':y

    subscription = Subscription(channel)
    subscription.subscribe(topic=f"Topic.{TOPIC}")

    log.info("Waiting for Images")

    while True:
      msg = channel.consume()
      img_unpack = msg.unpack(Image)
      imgNP = to_np(img_unpack)

      filename = '/data/image_rcvd.jpg' #Directory to save to volume

      cv2.imwrite(filename, imgNP)
      log.info("Image saved")
