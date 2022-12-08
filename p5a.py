#!/usr/bin/python3
from utils import *

input = load_input()


def format():
    state, instrs = input.split("\n\n")
    state = state.split("\n")
    i = 1
    out = {}
    while i < len(state[0]):
        out[int(state[-1:][0][i])] = [
            state[j][i] for j in range(len(state) - 1) if state[j][i] != " "
        ]
        i += 4

    return (
        out,
        [
            map(int, (x[1], x[3], x[5]))
            for x in map(lambda x: x.split(" "), instrs.split("\n"))
        ],
    )


def compute(state, instr):
    count, fr, to = instr
    state[to] = state[fr][:count][::-1] + state[to]
    state[fr] = state[fr][count:]
    return state


def doit():
    state, instrs = format()
    [compute(state, instr) for instr in instrs]
    return "".join([x[0] for x in state.values()])


if __name__ == "__main__":
    print(doit())
