point = []
instructions = []
Field = []

with open("AdventOfCode\\2021\\13\\input.txt","r") as f:
    for line in f:
        if line == "\n":
                continue
        if "fold" in line:
            instructions.append(line.replace("fold along ","").replace("\n",""))
            continue
        point.append([int(x) for x in(line.replace("\n","").split(","))])


#folding
def folding(point, fold):
    difference = 0
    additional = []
    for xx,yy in point:
        #x folds
        if "x" in fold:
            x=int(fold[2:])
            if x > xx:
                additional.append([xx,yy])
                continue
            difference = xx - x
            additional.append([x-difference,yy])
        #y folds
        if "y" in fold:
            y=int(fold[2:])
            if y > yy:
                additional.append([xx,yy])
                continue
            difference = yy - y
            additional.append([xx,y-difference])
    point = []
    for i in range(len(additional)):
        point.append(additional[i])
    return(point)

for fold in instructions:
    point = folding(point, fold)
#part1---------
""" point = folding(point, instructions[0]) """
#--------------
    
#finding furthers point
point.sort(key = lambda x: x[0])
point.reverse()
x = point[0][0]
point.sort(key = lambda x: x[1])
point.reverse()
y = point[0][1]

#generating field
for yy in range(int(y)+1):
    xs = []
    for xx in range(int(x)+1):
        xs.append(".")
    Field.append(xs)

#posting points onto the field
def assigning(x, y):
    Field[int(y)][int(x)] = "0"

for x,y in point:
    assigning(x, y)

#part1------
""" numberOFpoints = 0
for y in Field:
    for x in y:
        if x == "0":
            numberOFpoints += 1
print(numberOFpoints) """
#-----------

#creating output file
with open("AdventOfCode\\13\\output.txt","w") as f:
    for yy in range(len(Field)):
        line = ""
        for xx in range(len(Field[yy])):
            line = line + Field[yy][xx]
        
        f.write(line+"\n")
    
