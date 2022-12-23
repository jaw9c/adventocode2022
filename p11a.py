#!/usr/bin/python3
from utils import *

input = load_input()


def parse_operation(operation_str):
    if operation_str.split(" = ")[1] == "old * old":
        return lambda x: x * x
    else:
        operator_str = operation_str.split(" = ")[1][4]
        value = int(operation_str.split(" = ")[1][5:])        
        if operator_str == "+":
            return lambda x: x + value
        elif operator_str == "*":
            return lambda x: x * value

def parse(input):
    family = []
    for raw_monkey in input.split("\n\n"):
        parts = raw_monkey.split("\n")
        items = list(map(int, parts[1].split(": ")[1].split(", ")))
        op_func = parse_operation(parts[2].split(": ")[1])
        test_divider = int(parts[3].split("by ")[1])
        true_monkey = int(parts[4].split("monkey ")[1])
        false_monkey = int(parts[5].split("monkey ")[1])

        family.append([items, op_func, test_divider, true_monkey, false_monkey])
    return family

def doit(family):
    inspects = [0 for _ in range(len(family))]
    for _ in range(20):
        for i in range(len(family)):
            items, op_func, test_divider, true_monkey, false_monkey = family[i]
            for item in items:
                inspects[i] += 1
                new = op_func(item) // 3
                if new % int(test_divider) == 0:
                    family[true_monkey][0].append(new)
                else:
                    family[false_monkey][0].append(new)
            family[i][0] = []
    
    sorted_inspects = sorted(inspects, reverse=True)
    return sorted_inspects[0] * sorted_inspects[1]

if __name__ == "__main__":
    print(doit(parse(input)))
