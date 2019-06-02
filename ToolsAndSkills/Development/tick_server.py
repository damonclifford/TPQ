#
# Tick Data Server
#
import q
import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://0.0.0.0:5555')

AAPL = 100.

while True:
    AAPL += random.gauss(0, 1) * 0.5
    msg = 'AAPL {:.4f}'.format(AAPL)
    socket.send_string(msg)
    print(msg)
    q(msg)
    # q.d()
    time.sleep(random.random() * 2)
