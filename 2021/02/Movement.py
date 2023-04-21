move = []

with open("AdventOfCode\\2021\\2\\input.txt","r") as f:
    for l in f:
        move.append(l.split())

#Part1
xAxis = 0
yAxis = 0

for i in move:
    if i[0] == "forward":
        xAxis += int(i[1])
    elif i[0] == "down":
        yAxis += int(i[1])
    elif i[0] == "up":
        yAxis -= int(i[1])

print("part1 " + str(xAxis*yAxis))

#Part2
xAxis = 0
yAxis = 0
aim = 0

for i in move:
    if i[0] == "forward":
        xAxis += int(i[1])
        yAxis += int(i[1])*aim
    elif i[0] == "down":
        aim += int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])

print("Part2 " + str(xAxis*yAxis))
