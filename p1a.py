#!/usr/bin/python3
from utils import *
from functools import reduce

input = load_input_as_list()

test_input = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]


def doit(input):
    return reduce(
        lambda acc, xs: (max(*acc), 0) if xs == "" else (acc[0], acc[1] + int(xs)),
        input,
        (0, 0),
    )[0]


if __name__ == "__main__":
    print(doit(input))
