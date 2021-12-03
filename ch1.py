# Advent of Code 2021: Day 1 - Sonar Sweep: Part One and Two
import os, sys;

def part_one(inputs):
    return sum(1 for i in range(len(inputs)) if len(inputs) - 1 != i and inputs[i] < inputs[i+1])


def part_two(inputs):
    data = [sum(inputs[i: i+3]) for i in range(len(inputs)) if len(inputs[i: i+3]) == 3]
    results = sum([1 for i in range(len(data)) if len(data) - 1 != i and data[i] < data[i+1]])
    return results

inputs = []
with open('ch1-input.txt', 'r') as f:
    inputs = f.readlines()

inputs = list(map(int, inputs))

print(part_one(inputs))
print(part_two(inputs))
