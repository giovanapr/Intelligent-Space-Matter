from is_wire.core import Channel, Subscription, Message, Logger
from is_msgs.image_pb2 import Image
import cv2
import numpy as np
import time

log = Logger(name='Pub Images')

def to_image(input_image, encode_format='.jpeg', compression_level=0.8):
    if isinstance(input_image, np.ndarray):
        if encode_format == '.jpeg':
            params = [cv2.IMWRITE_JPEG_QUALITY, int(compression_level * (100 - 0) + 0)]
        elif encode_format == '.png':
            params = [cv2.IMWRITE_JPEG_COMPRESSION, int(compression_level * (9 - 0) + 0)]
        else:
            return Image()
        cimage = cv2.imencode(ext=encode_format, img=input_image, params=params)
        return Image(data=cimage[1].tobytes())
    elif isinstance(input_image, Image):
        return input_image
    else:
        return Image()

log.info("Indicate the broker's IP and port")
IP = input(f"IP (or ENTER for localhost): ") or "localhost"
PORT = input(f"PORT (or ENTER for 5672): ") or "5672"

log.info("Broker login")
user = input(f"Username (or ENTER for guest): ") or "guest"
password = input(f"Password (or ENTER for guest): ") or "guest"

channel = Channel(f'amqp://{user}:{password}@{IP}:{PORT}')

while True:
    log.info("Indicate Directory and file Image")
    img_caminho = input('Directory and file Image: ')
    full_path = f"/app/images/{img_caminho}"
    img = cv2.imread(full_path)

    img_msg = Message()
    img_msg.pack(to_image(img))

    channel.publish(img_msg, topic='Topic.Frame')
    log.info("Image sent")
    time.sleep(1)
