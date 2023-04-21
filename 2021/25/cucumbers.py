Field = []
line = []

with open("AdventOfCode\\2021\\25\\test.txt","r") as f:
    for y in f:
        for x in y:
            x = x.strip("\n")
            if x == "":
                continue
            line.append(x)
        Field.append(line)
        line = []


def right(map):
    global finished1
    finished1 = True

    newField = []
    line = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            line.append(".")
        newField.append(line)
        line = []

    for y,row in enumerate(map):
        for x,col in enumerate(row):
            if col == ">":
                try:
                    if map[y][x+1] == ".":
                        newField[y][x+1] = ">"
                        finished1 = False
                except:
                    if x == len(map[0])-1:
                        if map[y][0] == ".":
                            newField[y][0] = ">"
                            finished1 = False
    
    return(newField)


def down(map):
    global finished2
    finished2 = True

    newField = []
    line = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            line.append(".")
        newField.append(line)
        line = []

    for y,row in enumerate(map):
        for x,col in enumerate(row):
            if col == "V":
                try:
                    if map[y+1][x] == ".":
                        newField[y+1][x] = "V"
                        finished2 = False
                except:
                    if x == len(map)-1:
                        if map[0][x] == ".":
                            newField[0][x] = "V"
                            finished2 = False
    
    return(newField)


finished1 = False
finished2 = False
counter = 0
while finished1 == False or finished2 == False:
    Field = right(Field)
    Field = down(Field)
    counter += 1

for y in Field:
    print(y)
print(counter)