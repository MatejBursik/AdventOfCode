crabLoc = []
crab = ""
fridge = ""

with open("AdventOfCode\\2021\\7\\input.txt","r") as f:
    l = f.read()
    fridge = l + ","
    for x in fridge: 
        if x == ",":
            crabLoc.append(int(crab))
            crab = ""
            continue
        crab = crab + x

""" counter = 0
for k in crabLoc:
        frequency = crabLoc.count(k)
        if frequency > counter:
            counter = frequency
            often = int(k)
print("Most frequent location is : " + str(often)) """

final = []
""" sum = 0
for i in crabLoc:
    sum += int(i)
average = sum//len(crabLoc) """

for r in range(1000):
    fuel = []
    oneFuel = 0
    for i in crabLoc:
        oneFuel = (i - r)
        if oneFuel < 0:
            oneFuel = oneFuel*-1
        fuel.append(oneFuel)

    allFuel = 0
    for i in fuel:
        allFuel += i
    
    final.append(allFuel)

final.sort()

print(final[0])