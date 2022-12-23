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

def move(H, T, instr, log=set()):
    log.add(T)
    Hx, Hy = H
    Tx, Ty = T
    direction, count = instr

    if count == 0:
        return H, T
    
    if direction == "R":
        Hx += 1
        if Hx - Tx > 1:
            Tx += 1
            if Hy != Ty:
                Ty += 1 if Hy > Ty else -1
        return move((Hx, Hy), (Tx, Ty), (direction, count - 1), log)
    elif direction == "L":
        Hx -= 1
        if Tx - Hx > 1:
            Tx -= 1
            if Hy != Ty:
                Ty += 1 if Hy > Ty else -1
        return move((Hx, Hy), (Tx, Ty), (direction, count - 1), log)
    elif direction == "D":
        Hy += 1
        if Hy - Ty > 1:
            Ty += 1
            if Hx != Tx:
                Tx += 1 if Hx > Tx else -1
        return move((Hx, Hy), (Tx, Ty), (direction, count - 1), log)
    elif direction == "U":
        Hy -= 1
        if Ty - Hy > 1:
            Ty -= 1
            if Hx != Tx:
                Tx += 1 if Hx > Tx else -1
        return move((Hx, Hy), (Tx, Ty), (direction, count - 1), log)

def doit(instrs):
    H, T = (0, 0), (0, 0)
    log = set()
    for instr in instrs:
        H, T = move(H, T, instr, log)
    return len(log)

if __name__ == "__main__":
    print(doit(parse(input)))
