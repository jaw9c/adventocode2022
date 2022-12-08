#!/usr/bin/python3
from utils import *

input = load_input_as_list()


def split(x):
    half = len(x) // 2
    return (x[:half], x[half:])


def doit(input):
    xs = [set(x) & set(y) for x, y in map(split, input)]
    return sum([ord(a) - 38 if a.isupper() else ord(a) - 96 for (a,) in xs])


if __name__ == "__main__":
    print(doit(input))
