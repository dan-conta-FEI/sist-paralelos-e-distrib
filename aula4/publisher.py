import zmq
from time import strftime, sleep

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    hora = strftime("%H:%M:%S")
    message = f"hora {hora}"

    print(f"P1: {message}", flush=True)

    pub.send_string(message)

    sleep(1)

pub.close()
context.close()
