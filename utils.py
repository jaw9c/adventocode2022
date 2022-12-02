#!/usr/bin/python3
import sys


def load_input_as_list():
    with open(sys.argv[1]) as f:
        return f.read().split("\n")


def load_input_as_ints():
    return list(map(load_input_as_list()))


def flatten(t):
    return [item for sublist in t for item in sublist]
