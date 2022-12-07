#!/usr/bin/python3

#!/usr/bin/python3
from utils import *

input = load_input_as_list()


def format(input):
    return [x.split(" ") for x in input]


def res(A, B):
    if A == "A":
        if B == "X":
            return 0 + 3
        if B == "Y":
            return 3 + 1
        if B == "Z":
            return 6 + 2
    if A == "B":
        if B == "X":
            return 0 + 1
        if B == "Y":
            return 3 + 2
        if B == "Z":
            return 6 + 3
    if A == "C":
        if B == "X":
            return 0 + 2
        if B == "Y":
            return 3 + 3
        if B == "Z":
            return 6 + 1


def doit(input):
    formatted_input = format(input)
    return sum([res(A, B) for A, B in formatted_input])


if __name__ == "__main__":
    print(doit(input))
