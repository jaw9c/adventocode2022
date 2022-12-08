#!/usr/bin/python3
from utils import *

input = load_input_as_list()


def thirdify(input):
    out = []
    while input:
        out.append(input[:3])
        input = input[3:]
    return out


def doit(input):
    xs = [set(x) & set(y) & set(z) for x, y, z in thirdify(input)]
    return sum([ord(a) - 38 if a.isupper() else ord(a) - 96 for (a,) in xs])


if __name__ == "__main__":
    print(doit(input))
