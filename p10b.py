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

    new_log = ""
    for i, val in enumerate(log):
        if i % 40 == val or i % 40 + 1 == val or i % 40 - 1 == val:
            new_log += "#"
        else:
            new_log += "."
    return [(new_log[x * 40:(x+1) * 40]) for x in range(6)]

if __name__ == "__main__":
    [print(x) for x in doit(parse(input))]
