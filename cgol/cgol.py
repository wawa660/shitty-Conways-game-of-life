#Conway's game of life :)
from colorama import Fore, Back, Style
from random import random

def render(state):
    print(Fore.BLACK + Back.GREEN)
    ch = {0 : ' ', 1 : '▀'}
    print('--' * len(state[0]) + '-' * 3)
    for i in state:
        print('| ', end = '')
        for j in i:
            print(ch[j], end = " ")
        print('|', end = '')
        print()
    print('--' * len(state[0]) + '-' * 3)
    print(Style.RESET_ALL)

def dead_state(height, width):
    state = [[0 for x in range(width)] for x in range(height)]
    return state

def random_state(height = 3, width = 3):
    state = dead_state(height, width)
    for i in range(height):
        for j in range(width):
            rand_num = random()
            if rand_num < 0.5:
                state[i][j] = 0
            else: 
                state[i][j] = 1
    return state

def next_state(state):
    cstate = [row[:] for row in state]  # Create a copy of the state grid

    def n_alive(i, j):
        alive_neighbours = 0
        for x in -1, 0, 1:
            for y in -1, 0, 1:
                if x == 0 and y == 0:
                    continue
                ni = i + x
                nj = j + y
                if 0 <= ni < len(state) and 0 <= nj < len(state[i]):
                    if state[ni][nj] == 1:
                        alive_neighbours += 1
        return alive_neighbours

    for i in range(len(cstate)):
        for j in range(len(cstate[i])):
            if state[i][j] == 1:
                if n_alive(i, j) < 2 or n_alive(i, j) > 3:
                    cstate[i][j] = 0
            else:
                if n_alive(i, j) == 3:
                    cstate[i][j] = 1
    return cstate