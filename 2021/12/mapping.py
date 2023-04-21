"""
don't visit small caves more than once.
There are two types of caves:
    big caves (written in uppercase, like A)
    small caves (written in lowercase, like b)
"""
import random

inData = []
with open("AdventOfCode\\2021\\12\\input.txt","r") as f:
    for line in f:
        Line = line.replace("start","Start")
        line = Line.replace("end","End")
        inData.append(line.strip().split("-"))

allPoints = {"Start":"", "End":""}

for con in inData:
    for Point in con:
        if Point not in allPoints:
            allPoints[Point] = ""
    
for i in allPoints:    
    for con in inData:
        if i in con:
            for one in con:
                if one == "Start":
                    continue
                if i != one:
                    allPoints[i] += one + ","

for i in allPoints:
    allPoints[i] = allPoints[i][:len(allPoints[i])-1]
    allPoints[i] = allPoints[i].split(",")

#print(allPoints)

num = 0
memory = []
with open("AdventOfCode\\2021\\12\\memory.txt","r") as f:
    for i in f:
        memory.append(i.strip())

def solve(Points):
    #making a random path
    path = ""
    point = "Start"

    try:
        while point != "End":
            path += point
            choise = random.randint(0,len(Points[point])-1)
            oldPoint = point
            point = Points[point][choise]
            if oldPoint.islower():
                Points.pop(oldPoint)
    except:
        return #print("wrong turn")
        
    path += "End"
        
    if path not in memory:
        memory.append(path)

#activation of definition
while num != 1000000000:
    Copy = allPoints.copy()
    solve(Copy)
    num += 1

with open("AdventOfCode\\2021\\12\\memory.txt","w") as f:
    for i in memory:
        f.write(i + "\n")

print(len(memory))