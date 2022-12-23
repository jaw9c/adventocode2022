#!/usr/bin/python3
from utils import *

input = load_input_as_list()

def parse(input):
    return list(map(lambda x: (x[:1], int(x[2:])), input))

def pretty_print(H, T):
    for y in range(-4, 1):
        for x in range(0, 6):
            if (x, y) == H:
                print("H", end="")
            elif (x, y) == T:
                print("T", end="")
            elif (x, y) == (0, 0):
                print("s", end="")
            else:
                print(".", end="")
        print()

def move_tail(H, T, direction):
    Hx, Hy = H
    Tx, Ty = T
    if Hx - Tx > 1:
        Tx += 1
        if Hy != Ty:
            Ty += 1 if Hy > Ty else -1
    if Tx - Hx > 1:
        Tx -= 1
        if Hy != Ty:
            Ty += 1 if Hy > Ty else -1
    if Hy - Ty > 1:
        Ty += 1
        if Hx != Tx:
            Tx += 1 if Hx > Tx else -1
    if Ty - Hy > 1:
        Ty -= 1
        if Hx != Tx:
            Tx += 1 if Hx > Tx else -1
    return (Tx, Ty)

def doit(instrs):
    knots = [(0,0) for _ in range(10)]
    log = set()
    for direction, count in instrs:
        for _ in range(count):
            if direction == "R":
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif direction == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])
            elif direction == "D":
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif direction == "U":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            for i in range(len(knots) - 1):
                knots[i+1] = move_tail(knots[i], knots[i+1], direction)
                if i == len(knots) - 2:
                    log.add(knots[i+1])
    return len(log)

if __name__ == "__main__":
    print(doit(parse(input)))
