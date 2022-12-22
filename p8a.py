#!/usr/bin/python3
from utils import *

input = load_input_as_list()

def parse(input):
    return list(map(lambda x: list(map(int, x)), input))

def is_visible(i, j, state):
    if i == 0 :
        return True
    if j == 0:
        return True
    if i == len(state)-1:
        return True
    if j == len(state)-1:
        return True
    if all([
        len([(k, j) for k in range(i+1, len(state[0])) if state[j][k] >= state[j][i]]) > 0,
        len([(i, k) for k in range(j+1, len(state)) if state[k][i] >= state[j][i]]) > 0,
        len([(k, j) for k in range(0, i) if state[j][k] >= state[j][i]]) > 0,
        len([(i, k) for k in range(0, j) if state[k][i] >= state[j][i]]) > 0,
    ]):
        return False
    return True

def doit(input):
    return sum([1 if is_visible(i, j, input) else 0 for i in range(len(input[0])) for j in range(len(input))])

if __name__ == "__main__":
    print(doit(parse(input)))
