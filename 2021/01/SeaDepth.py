with open("AdventOfCode\\2021\\1\\input.txt","r") as f:
    Data = f.read()
strip = Data.replace("\n"," ")
Data = strip + " "

#Part1
depths = []
word = ""

for i in Data:
    if i == " ":
        depths.append(int(word))
        word = ""
        continue
    else:
        word = word + i

count = 0
incNum = 0

for i in depths:
    count += 1
    if count == len(depths):
        continue
    if i < depths[count]:
        incNum += 1

print("Part1" + str(incNum))

#Part2
ThreeMSW = []
count = 0
count1 = 0
count2 = 1
incNum = 0

for i in depths:
    count1 += 1
    count2 += 1
    if count2 == len(depths):
        break
    ThreeMSW.append(i + depths[count1] + depths[count2])

for i in ThreeMSW:
    count += 1
    if count == len(ThreeMSW):
        continue
    if i < ThreeMSW[count]:
        incNum += 1

print("Part2" + str(incNum))