import os

inputfile = "day02.txt"

def part1(inputdata):
    for line in inputdata:
        data = str.split(line, ",")

    for i in range(0, len(data)): 
        data[i] = int(data[i]) 

    index = 0
    while True:
        if data[index] == 1:
            result = data[data[index + 1]] + data[data[index + 2]]
            data[data[index + 3]] = result
        elif data[index] == 2:
            result = data[data[index + 1]] * data[data[index + 2]]
            data[data[index + 3]] = result
        elif data[index] == 99:
            return str(data)
        print(index)
        index += 4

    return data

def part2(inputdata):
    for line in inputdata:
        data = str.split(line, ",")

    for i in range(0, len(data)): 
        data[i] = int(data[i]) 

    datacpy = list.copy(data)

    int1 = 40
    int2 = 40

    while True:
        int1 += 1
        int2 += 1
        
        for i in range(40, int1):
            for j in range(40, int2):
                data = list.copy(datacpy)
                data[1] = i
                data[2] = j

                index = 0
                try:
                    while True:
                        if data[index] == 1:
                            result = data[data[index + 1]] + data[data[index + 2]]
                            data[data[index + 3]] = result
                        elif data[index] == 2:
                            result = data[data[index + 1]] * data[data[index + 2]]
                            data[data[index + 3]] = result
                        elif data[index] == 99:
                            break
                        index += 4
                except IndexError:
                    pass

                if data[0] == 19690720:
                    return (data[1], data[2])


if __name__ == "__main__":
    with open(inputfile, "r") as inputdata:
        print("Part 1: " + str(part1(inputdata)))
    with open(inputfile, "r") as inputdata:
        print("Part 2: " + str(part2(inputdata)))