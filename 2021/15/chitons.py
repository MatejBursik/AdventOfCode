OriTables = []
outputField = []
lines = []
Li = []

with open("AdventOfCode\\2021\\15\\input.txt","r") as f:
    for line in f:
        for character in line:
            if character == "\n":
                continue
            lines.append(int(character))
            Li.append(0)
        OriTables.append(lines)
        outputField.append(Li)
        lines = []
        Li = []

#creating the outputField
outputField[0][0] = OriTables[0][0]

for i in range(10):
    for y in range(len(OriTables)):
        for x in range(len(OriTables[y])):
            #rigth left
            if x < len(OriTables[y])-1:
                carry = int(outputField[y][x]) + int(OriTables[y][x+1])
                if outputField[y][x+1] > carry or outputField[y][x+1] == 0:
                    outputField[y][x+1] = carry
            if x != 0:
                carry = int(outputField[y][x]) + int(OriTables[y][x-1])
                if outputField[y][x-1] > carry or outputField[y][x-1] == 0:
                    outputField[y][x-1] = carry
            #down up
            if y < len(OriTables)-1:
                carry = int(outputField[y][x]) + int(OriTables[y+1][x])
                if outputField[y+1][x] > carry or outputField[y+1][x] == 0:
                    outputField[y+1][x] = carry
            if y != 0:
                carry = int(outputField[y][x]) + int(OriTables[y-1][x])
                if outputField[y-1][x] > carry or outputField[y-1][x] == 0:
                    outputField[y-1][x] = carry

with open("AdventOfCode\\2021\\15\\output.txt","w") as f:
    for yy in range(len(outputField)):
        line = ""
        for xx in range(len(outputField[yy])):
            line = line + str(outputField[yy][xx]) + ","
        f.write(line+"\n")

print(outputField[len(outputField)-1][len(outputField[0])-1] - OriTables[0][0])
