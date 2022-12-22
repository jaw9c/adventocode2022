#!/usr/bin/python3
from utils import *

input = load_input_as_list()

def construct(input):
    state = {}
    cwd_stack = [state]
    for instr in input[1:]:
        if instr[:1] == "$":
            dir = instr[1:]
            if dir[1:3] == "cd":
                if dir[4:] == "..":
                    cwd_stack.pop()
                else:
                    cwd_stack.append(cwd_stack[-1][dir[4:]])
        else:
            if instr[:3] == "dir":
                cwd_stack[-1][instr[4:]] = {}
            else:
                size, name = instr.split(" ")
                cwd_stack[-1][name] = int(size)
    return state

def search(node, log):
    if type(node) == int:
        return node
    else:
        total = sum([search(v, log) for k, v in node.items()])
        log.append(total)
        return total

def doit(input):
    log = []
    used_size = search(construct(input), log)
    
    return min([v for v in log if used_size - v < 40000000])

if __name__ == "__main__":
    print(doit(input))