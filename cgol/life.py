#!/usr/bin/env python3

import sys, time
from cgol import random_state, next_state, render

if len(sys.argv) == 2:
    n = int(sys.argv[1])
elif len(sys.argv) == 1:
    n = 15
else:
    print("Invalid Command")

state = random_state(n, n)
while True:
    render(state)
    nextstate = next_state(state)
    if state == nextstate:
        break
    state = nextstate
    time.sleep(0.2)
