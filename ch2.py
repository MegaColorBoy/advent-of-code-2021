# Advent of Code - Day 2: Dive!

import os, sys

# Solution for part one
def part_one(inputs):
    hp = d = 0
    for x in inputs:
        dir = x.split()[0]
        v = int(x.split()[1])
        if dir == "forward":
            hp += v
        elif dir == "down":
            d += v
        elif dir == "up":
            d -= v
    return hp * d

# Solution for part two
def part_two(inputs):
    hp = d = a = 0
    for x in inputs:
        dir = x.split()[0]
        v = int(x.split()[1])
        if dir == "forward":
            hp += v
            d += a * v
        elif dir == "down":
            a += v
        elif dir == "up":
            a -= v
    return hp * d

with open('ch2-input.txt') as f:
    inputs = f.readlines()
    print(part_one(inputs))
    print(part_two(inputs))
