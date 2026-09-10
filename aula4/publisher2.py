import zmq
import random
from time import sleep

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    numero = random.randint(1, 6)
    message = f"numero {numero}"

    print(f"P2: {message}", flush=True)

    pub.send_string(message)

    sleep(1)

pub.close()
context.close()
