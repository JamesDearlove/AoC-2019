import os
from math import floor

inputfile = "day01.txt"

def part1(inputdata):
    total = 0
    for line in inputdata:
        total += floor(int(line) / 3) - 2

    return total

def part2calc(input):
    step = floor(input / 3) - 2
    if (step <= 0):
        return 0
    else:
        return step + part2calc(step)

def part2(inputdata):
    total = 0
    for line in inputdata:
        total += part2calc(int(line))

    return total

if __name__ == "__main__":
    with open(inputfile, "r") as inputdata:
        print("Part 1: " + str(part1(inputdata)))
    with open(inputfile, "r") as inputdata:
        print("Part 2: " + str(part2(inputdata)))