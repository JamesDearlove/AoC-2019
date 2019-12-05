import os

inputfile = "day03.txt"
paths = []

def pathcoords(index):
    givendirections = str.split(paths[index],',')
    points = [(0,0)]
    # (x, y)

    point = 1
    for element in givendirections:
        direction = element[:1]
        distance = int(element[1:])
        prevpoint = points[point - 1]

        if direction == "U":
            points.append((prevpoint[0], prevpoint[1] + distance))
        elif direction == "R":
            points.append((prevpoint[0] + distance, prevpoint[1]))
        elif direction == "L":
            points.append((prevpoint[0] - distance, prevpoint[1]))
        elif direction == "D":
            points.append((prevpoint[0], prevpoint[1] - distance))
        
        point += 1

    return points

def pointsbetweencoords(point1, point2):
    points = []
    
    if point1[1] == point2[1]:
        if point1[0] < point2[0]:
            step = 1
        else: 
            step = -1
        
        for x in range(point1[0], point2[0], step):
            points.append((x, point1[1]))
    else:
        if point1[1] < point2[1]:
            step = 1
        else: 
            step = -1

        for y in range(point1[1], point2[1], step):
            points.append((point1[0], y))

    return points

def manhattan(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def part1(inputdata):
    path1 = pathcoords(0)
    path2 = pathcoords(1)
    
    filledpath1 = []
    filledpath2 = []

    index = 0
    while index < (path1.__len__() - 1):
        filledpath1.extend(pointsbetweencoords(path1[index], path1[index + 1]))
        index += 1
    filledpath1.append(path1[-1])
    filledpath1.remove((0,0))

    index = 0
    while index < (path2.__len__() - 1):
        filledpath2.extend(pointsbetweencoords(path2[index], path2[index + 1]))
        index += 1
    filledpath2.append(path2[-1])
    filledpath2.remove((0,0))

    intersects = list(set(filledpath1) & set(filledpath2))
    print(intersects)

    mindist = manhattan((0,0), intersects[0])
    for point in intersects:
        newdist = manhattan((0,0), point)
        if newdist < mindist:
            mindist = newdist

    return str(mindist)

def part2(inputdata):
    path1 = pathcoords(0)
    path2 = pathcoords(1)
    
    filledpath1 = []
    filledpath2 = []

    index = 0
    while index < (path1.__len__() - 1):
        filledpath1.extend(pointsbetweencoords(path1[index], path1[index + 1]))
        index += 1
    filledpath1.append(path1[-1])
    filledpath1.remove((0,0))

    index = 0
    while index < (path2.__len__() - 1):
        filledpath2.extend(pointsbetweencoords(path2[index], path2[index + 1]))
        index += 1
    filledpath2.append(path2[-1])
    filledpath2.remove((0,0))

    intersects = list(set(filledpath1) & set(filledpath2))
    print(intersects)

    minloc = -1
    mindist = 99999999999999999999
    for point in range(0, intersects.__len__()):
        newdist = filledpath1.index(intersects[point]) + filledpath2.index(intersects[point])
        if newdist < mindist:
            minloc = point
            mindist = newdist

    return str(mindist + 2)

if __name__ == "__main__":
    with open(inputfile, "r") as inputdata:
        index = 0
        for line in inputdata:
            paths.append(line)
            index += 1

    print("Part 1: " + part1(inputdata))
    print("Part 2: " + part2(inputdata))