#!/usr/bin/python3
from utils import *

input = load_input_as_list()

def parse(input):
    return list(map(lambda x: (x[:4], int(x[5:]) if x[:4] != "noop" else (x[:4], None)), input))

def doit(instrs):
    log = [1]
    X = 1
    for (instr, value) in instrs:
        if instr == "noop":
            log.append(X)
        elif instr == "addx":
            log.append(X)
            X += value
            log.append(X)
    return sum([log[x - 1] * x for x in [20, 60, 100, 140, 180, 220]])

if __name__ == "__main__":
    print(doit(parse(input)))
