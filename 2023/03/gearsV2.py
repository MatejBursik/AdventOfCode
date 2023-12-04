def surrouding(arr,x,y):
    t = "*"
    if x-1 >= 0 and y+1 < len(arr):
        if arr[y+1][x-1] == t:
            return (True,(x-1,y+1))
    if x-1 >= 0:
        if arr[y][x-1] == t:
                return (True,(x-1,y))
    if x-1 >= 0 and y-1 >= 0:
        if arr[y-1][x-1] == t:
                return (True,(x-1,y-1))
    if y-1 >= 0:
        if arr[y-1][x] == t:
                return (True,(x,y-1))
    if y-1 >= 0 and x+1 < len(arr[0]):
        if arr[y-1][x+1] == t:
                return (True,(x+1,y-1))
    if x+1 < len(arr[0]):
        if arr[y][x+1] == t:
                return (True,(x+1,y))
    if x+1 < len(arr[0]) and y+1 < len(arr):
        if arr[y+1][x+1] == t:
                return (True,(x+1,y+1))
    if y+1 < len(arr):
        if arr[y+1][x] == t:
                return (True,(x,y+1))
        
    return (False,(-1,-1))

schematic = []
with open("2023\\03\\input.txt", "r") as f:
    for line in f:
        schematic.append(list(line.strip()))
print(schematic)

parts = []
number = ""
numInEngine = False

for y,line in enumerate(schematic):
    for x,value in enumerate(line):
        if value.isdigit():
            number += value
            if not numInEngine:
                numInEngine,coord = surrouding(schematic,x,y)
        else:
            if numInEngine:
                parts.append([int(number),coord])
            numInEngine = False
            number = ""

print(parts)
ratioSum = 0
for num1,coord1 in parts:
    for num2,coord2 in parts:
        if num1 != num2 and coord1 == coord2:
            ratioSum += num1*num2
            break
print("Gear ratio sum:",ratioSum//2)