grid = []
line = []

with open("AdventOfCode\\2021\\11\\input.txt","r") as f:
    for y in f:
        for x in y.strip():
            line.append(int(x))
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
    grid[Pos[0]][Pos[1]] = 0
    for y,line in enumerate(grid):
        for x,term in enumerate(line):
            if y+1==Pos[0] and x+1==Pos[1] and term > 0:
                grid[y][x] += 1
            if y+1==Pos[0] and x==Pos[1] and term>0:
                grid[y][x] += 1
            if y+1==Pos[0] and x-1==Pos[1] and term>0:
                grid[y][x] += 1

            if y==Pos[0] and x+1==Pos[1] and term>0:
                grid[y][x] += 1
            if y==Pos[0] and x-1==Pos[1] and term>0:
                grid[y][x] += 1

            if y-1==Pos[0] and x+1==Pos[1] and term>0:
                grid[y][x] += 1
            if y-1==Pos[0] and x==Pos[1] and term>0:
                grid[y][x] += 1
            if y-1==Pos[0] and x-1==Pos[1] and term>0:
                grid[y][x] += 1
    return(grid)
    #set enegy level = 0 and increasing surrounding energy levels by 1


def check(grid):
    global Ten
    #chech for flashes
    Ten = True
    for y,line in enumerate(grid):
        for x,term in enumerate(line):
            if int(term) > 9:
                Pos = [y,x]
                grid = flash(grid,Pos)
                Ten = False
    return(grid)
            

def step(grid):
    global Ten
    Ten = False
    #incerase energy levels
    for y,row in enumerate(grid):
        for x,col in enumerate(row):
            grid[y][x] += 1

    #check loop
    while not Ten:
        grid = check(grid)
    return(grid)

done = False
numba = 0
while not done:
    grid = step(grid)
    numba += 1
    done = True
    for y in grid:
        for x in y:
            if x != 0:
                done = False

print(numba)