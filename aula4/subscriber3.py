import zmq

context = zmq.Context()

sub = context.socket(zmq.SUB)

sub.setsockopt_string(zmq.SUBSCRIBE, "")
sub.connect("tcp://proxy:5556")

while True:
    message = sub.recv_string()
    print(f"S3: {message}", flush=True)

sub.close()
context.close()
