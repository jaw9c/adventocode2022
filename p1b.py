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
    totals, other = reduce(
        lambda acc, x: (acc[0] + [acc[1]], 0) if x == "" else (acc[0], acc[1] + int(x)),
        input,
        ([], 0),
    )
    totals += [other]
    totals.sort()
    return sum(totals[-3:])


if __name__ == "__main__":
    print(doit(input))
