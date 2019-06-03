#
#
#
import time 
import random

AAPL = 100.

while True:
    AAPL += random.gauss(0, 1) * 0.5
    msg = 'AAPL {:4f}'.format(AAPL)
    print(msg)


