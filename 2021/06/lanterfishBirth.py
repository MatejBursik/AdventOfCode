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

for x in range(80):
    counter = 0
    newFish = 0
    for i in lanterfish:
        if i == "0":
            lanterfish[counter] = "6"
            newFish += 1
        else:
            Strr = int(i) - 1
            lanterfish[counter] = str(Strr)
        counter += 1
        
    #adding Fish
    for i in range(newFish):
        lanterfish.append("8")

numberFish = len(lanterfish)
print(numberFish)



#recursive verion
""" count = 0
def rec(input):
    global count
    if count == 79:
        numberFish = len(input)
        print(numberFish)
    else:
        counter = 0
        newFish = 0
        for i in input:
            if i == "0":
                input[counter] = "6"
                newFish += 1
            else:
                Strr = int(i) - 1
                input[counter] = str(Strr)
            counter += 1

        #adding Fish
        for i in range(newFish):
            input.append("8")

        count += 1
        rec(input)

rec(lanterfish) """