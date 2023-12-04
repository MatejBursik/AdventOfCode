def surrouding(arr,x,y):
    types = ['*', '-', '$', '=', '+', '&', '@', '#', '/', '%']
    if x-1 >= 0 and y+1 < len(arr):
        if arr[y+1][x-1] in types:
            return True
    if x-1 >= 0:
        if arr[y][x-1] in types:
            return True
    if x-1 >= 0 and y-1 >= 0:
        if arr[y-1][x-1] in types:
            return True
    if y-1 >= 0:
        if arr[y-1][x] in types:
            return True
    if y-1 >= 0 and x+1 < len(arr[0]):
        if arr[y-1][x+1] in types:
            return True
    if x+1 < len(arr[0]):
        if arr[y][x+1] in types:
            return True
    if x+1 < len(arr[0]) and y+1 < len(arr):
        if arr[y+1][x+1] in types:
            return True
    if y+1 < len(arr):
        if arr[y+1][x] in types:
            return True
        
    return False

schematic = []
with open("2023\\03\\input.txt", "r") as f:
    for line in f:
        schematic.append(list(line.strip()))
print(schematic)

partSum = 0
number = ""
numInEngine = False

for y,line in enumerate(schematic):
    for x,value in enumerate(line):
        if value.isdigit():
            number += value
            if not numInEngine:
                numInEngine = surrouding(schematic,x,y)
        else:
            if numInEngine:
                partSum += int(number)
            numInEngine = False
            number = ""

print("Sum of all part",partSum)