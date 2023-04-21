lanterfish = []
oneFish = ""
fridge = ""

with open("AdventOfCode\\2021\\6\\input.txt","r") as f:
    l = f.read()
    fridge = l + ","
    for x in fridge: 
        if x == ",":
            lanterfish.append(oneFish)
            oneFish = ""
            continue
        oneFish = oneFish + x

f0=lanterfish.count("0")
f1=lanterfish.count("1")
f2=lanterfish.count("2")
f3=lanterfish.count("3")
f4=lanterfish.count("4")
f5=lanterfish.count("5")
f6=lanterfish.count("6")
f7=lanterfish.count("7")
f8=lanterfish.count("8")

for x in range(256):
    newFish = f0
    oldFish = f0
    f0 = f1
    f1 = f2
    f2 = f3
    f3 = f4
    f4 = f5
    f5 = f6
    f6 = oldFish + f7
    f7 = f8
    f8 = newFish

allFish = f0+f1+f2+f3+f4+f5+f6+f7+f8
print(allFish)

