#!/usr/bin/env python
import zmq
import sys

ctx = zmq.Context()
socket = ctx.socket(zmq.PULL)

# tcp://127.0.0.1:5500
socket.connect(sys.argv[1])
while True:
    x = socket.recv_string()
    print(x.rstrip('\n'))
