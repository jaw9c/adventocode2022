#!/usr/bin/python3
from utils import *

input = load_input_as_list()


def format(x):
    a, b = x.split(",")
    Ax, Ay = map(int, a.split("-"))
    Bx, By = map(int, b.split("-"))
    if Ay < Bx:
        return 0
    if By < Ax:
        return 0
    return 1


def doit(input):
    return sum(map(format, input))


if __name__ == "__main__":
    print(doit(input))
