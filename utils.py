#!/usr/bin/python3
import sys


def load_input():
    with open(sys.argv[1]) as f:
        return f.read()


def load_input_as_list():
    return load_input().split("\n")


def load_input_as_ints():
    return list(map(load_input_as_list()))


def flatten(t):
    return [item for sublist in t for item in sublist]
