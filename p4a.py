#!/usr/bin/python3

#!/usr/bin/python3
from utils import *

input = load_input_as_list()


def format(x):
    a, b = x.split(",")
    Ax, Ay = map(int, a.split("-"))
    Bx, By = map(int, b.split("-"))
    if Ax <= Bx and By <= Ay:
        return 1
    if Bx <= Ax and Ay <= By:
        return 1
    return 0


def doit(input):
    return sum(map(format, input))


if __name__ == "__main__":
    print(doit(input))
