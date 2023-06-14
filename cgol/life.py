#!/usr/bin/python3

import sys, time
from cgol import random_state, next_state, render

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 10

state = random_state(n, n)
while True:
    render(state)
    nextstate = next_state(state)
    if state == nextstate:
        break
    state = nextstate
    time.sleep(0.25)