#!/usr/bin/python3
from utils import *

input = load_input_as_list()

def parse(input):
    return list(map(lambda x: list(map(int, x)), input))

def scenic_score(i, j, state):
    if i == 0 :
        return 0
    if j == 0:
        return 0
    if i == len(state)-1:
        return 0
    if j == len(state)-1:
        return 0
    max_tres = [
        [j-k  for k in list(range(0, j))[::-1] if state[k][i] >= state[j][i]][:1] or [j],
        [i-k  for k in  list(range(0, i))[::-1] if state[j][k] >= state[j][i]][:1] or [i],
        [k-i  for k in range(i+1, len(state[0])) if state[j][k] >= state[j][i]][:1] or [len(state[0]) - i - 1],
        [k-j for k in range(j+1, len(state)) if state[k][i] >= state[j][i]][:1] or [len(state) - j - 1],
    ]
    return max_tres[0][0] * max_tres[1][0] * max_tres[2][0] * max_tres[3][0]

def doit(input):
    return max([scenic_score(i, j, input) for i in range(len(input[0])) for j in range(len(input))])

if __name__ == "__main__":
    print(doit(parse(input)))
