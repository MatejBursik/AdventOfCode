"""
P2
1000000000000 rocks (not 2022)

optimization:
- change chamber into coords, therefor less memory to store and compute through
- change left,right,down to cycle through _chamber not the _pit
- look for the higest from 0 not len()
"""

class Rock():
    def __init__(self,draw_coords):
        self.draw_coords = draw_coords

def left(_chamber, _pit):
    for x,y in _chamber:
        if x-1 < 0:
            return False
        if _pit[y][x-1] == "#":
            return False
        
    return True

def right(_chamber, _pit):
    for x,y in _chamber:
        if x+1 >= len(_pit[0]):
            return False
        if _pit[y][x+1] == "#":
            return False
        
    return True

def down(_chamber, _pit):
    for x,y in _chamber:
        if y+1 >= len(_pit):
            return False
        if _pit[y+1][x] == "#":
            return False
        
    return True

rocks = []
rocks.append(Rock([[0,0],[1,0],[2,0],[3,0]])) # Line
rocks.append(Rock([[0,1],[1,0],[1,1],[1,2],[2,1]])) # Plus
rocks.append(Rock([[0,0],[1,0],[2,0],[2,1],[2,2]])) # L
rocks.append(Rock([[0,0],[0,1],[0,2],[0,3]])) # Pipe
rocks.append(Rock([[0,0],[1,0],[0,1],[1,1]])) # Cube

chamber = [] # for falling rock coords
pit = [] # for staic rocks
highest = len(pit)-1 # from top
while len(pit)-highest <= 6:
    pit.insert(0,[".",".",".",".",".",".","."])

instruction = ""
with open("2022\\17\\input.txt","r") as f:
    instruction = f.readline().strip()

ins_pos = 0
rock_pos = 0
rock_count = 0
spawn = False
r = 2022#1000000000000 2022

while rock_count <= r:
    if ins_pos >= len(instruction):
        ins_pos = 0
    if rock_pos >= len(rocks):
        rock_pos = 0

    # only first rock spawn
    if rock_count == 0:
        highest = len(pit)-1
        draw_pos = [2,highest-3]

        for x,y in rocks[rock_pos].draw_coords:
            chamber.append([draw_pos[0]+x,draw_pos[1]-y])

        rock_pos += 1
        rock_count += 1

    # spawn rock
    if spawn:
        # transfer chamber to pit
        for x,y in chamber:
            pit[y][x] = "#"

        # find the highest
        for i,level in enumerate(pit):
            if "#" in level:
                highest = len(pit)-i
                break

        # pit expansion
        while len(pit)-highest <= 6:
            pit.insert(0,[".",".",".",".",".",".","."])

        # reset chamber
        chamber = []

        # spawn a rock
        draw_pos = [2,len(pit)-highest-3-1]

        for x,y in rocks[rock_pos].draw_coords:
            chamber.append([draw_pos[0]+x,draw_pos[1]-y])

        # update
        rock_pos += 1
        rock_count += 1
        spawn = False

    # movement based on instruction
    if instruction[ins_pos] == "<" and left(chamber,pit):
        for pos in chamber:
            pos[0] -= 1
    elif instruction[ins_pos] == ">" and right(chamber,pit):
        for pos in chamber:
            pos[0] += 1
    ins_pos += 1

    # movement down
    if down(chamber,pit):
        for pos in chamber:
            pos[1] += 1

    # new rock
    else:
        spawn = True

for i,level in enumerate(pit):
    if "#" in level:
        print("Highest point in the pit:", len(pit)-i)
        break
    