#!/usr/bin/python3
from utils import *

input = load_input_as_list()

test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print(input)


def doit(input):
    count = 0
    for i in range(len(input[1:])):
        if input[i + 1] > input[i]:
            count += 1
    return count


if __name__ == "__main__":
    print(doit(input))
