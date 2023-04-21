OriTables = []
outputField = []
lines = []

for t in range(5):
    with open("AdventOfCode\\2021\\15\\oriInput.txt","r") as f:
        for line in f:
            for i in range(5):
                for character in line.strip():   
                    hold = str(int(character) + i + t)
                    if len(hold) == 2:
                        lines.append(str(int(hold[1])+1))
                    else:
                        lines.append(hold)
            OriTables.append(lines)
            lines = []

outputField = OriTables

with open("AdventOfCode\\2021\\15\\input.txt","w") as f:
    for yy in range(len(outputField)):
        line = ""
        for xx in range(len(outputField[yy])):
            line = line + str(outputField[yy][xx])
        f.write(line+"\n")
