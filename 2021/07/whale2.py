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

final = []

for r in range(max(crabLoc)+1):
    fuel = []
    oneFuel = 0
    for i in crabLoc:
        f = (i - r)
        if f < 0:
            f *= -1
        oneFuel = (f**2+f)//2
        
        fuel.append(oneFuel)

    allFuel = 0
    for i in fuel:
        allFuel += i
    
    final.append(allFuel)

final.sort()

print(final[0])
















""" crabLoc = []
crab = ""
fridge = ""

with open("AdventOfCode\\7\\input.txt","r") as f:
    l = f.read()
    fridge = l + ","
    for x in fridge: 
        if x == ",":
            crabLoc.append(int(crab))
            crab = ""
            continue
        crab = crab + x

final = []

for r in range(1000):
    fuel = []
    oneFuel = 0
    for i in crabLoc:
        f = i - r

        oneFuel = (f^2+f)/2
        if f < 0:
            f = f*-1
        
        fuel.append(oneFuel)

    allFuel = 0
    for i in fuel:
        allFuel += i
    
    final.append(allFuel)

final.sort()

print(final[0]) """