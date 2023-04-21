grid = []
line = []

with open("AdventOfCode\\2021\\11\\input.txt","r") as f:
    for y in f:
        for x in y:
            hold = x.strip()
            if hold == "":
                continue
            line.append(hold)
        grid.append(line)
        line = []

""" 
energy levels += 1
if energy level > 9 = flash(set enegy level = 0 and doesnt increase by other flashes) 
    surrounding energy levels += 1
 """

Flash = 0
Ten = False

def flash(grid,Pos):
    global Flash
    Flash += 1

    for y,line in enumerate(grid):
        for x,term in enumerate(line):
            if y+1==Pos[0] and x+1==Pos[1]:
                term = str(int(term)+ 1)
            if y+1==Pos[0] and x==Pos[1]:
                term = str(int(term)+ 1)
            if y+1==Pos[0] and x-1==Pos[1]:
                term = str(int(term)+ 1)

            if y==Pos[0] and x+1==Pos[1]:
                term = str(int(term)+ 1)
            if y==Pos[0] and x-1==Pos[1]:
                term = str(int(term)+ 1)

            if y-1==Pos[0] and x+1==Pos[1]:
                term = str(int(term)+ 1)
            if y-1==Pos[0] and x==Pos[1]:
                term = str(int(term)+ 1)
            if y-1==Pos[0] and x-1==Pos[1]:
                term = str(int(term)+ 1)
    grid[Pos[0]][Pos[1]] = "0a"
    return(grid)
    #set enegy level = 0 and increasing surrounding energy levels by 1


def check(grid):
    global Ten
    #chech for flashes
    Ten = True
    for y,line in enumerate(grid):
        for x,term in enumerate(line):
            try:
                if int(term) > 9:
                    Pos = [y,x]
                    grid = flash(grid,Pos)
                    Ten = False
                    break
            except:
                pass

    return(grid)


def step(grid):
    global Ten
    #incerase energy levels
    for y in grid:
        for x in y:
            x = str(int(x)+ 1)

    #check loop
    while not Ten:
        grid = check(grid)

    #removing a
    for y in grid:
        for x in y:
            if "a" in x:
                x = x[0]

    return(grid)


for i in range(100):
    grid = step(grid)

print(Flash)