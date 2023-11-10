"""
P2
1000000000000 rocks (not 2022)

optimization:
- change chamber into coords, therefor less memory to store and compute through
- change left,right,down to cycle through _chamber not the _pit
- change pit into integers
- remove Rock object
- replace integers in pit for booleans
- rewrite for/if to oneliners (they are more efficient)(sometimes)
- change the use of len because it takes a long time
- Instead of recalculating the highest point in the pit after each rock falls, update it only when a new highest is reached
    Try to do it by combining "transfer chamber to pit" and "find the highest" (solution: change the concept of the highest to calculate emptiness, not fullness)

1) implement pit reduction
"""
import time
timer = time.time()
def left(_chamber, _pit):
    for x,y in _chamber:
        if x-1 < 0:
            return False
        if _pit[y][x-1]:
            return False
        
    return True

def right(_chamber, _pit):
    for x,y in _chamber:
        if x+1 >= 7:
            return False
        if _pit[y][x+1]:
            return False
        
    return True

def down(_chamber, _pit, _depth):
    for x,y in _chamber:
        if y+1 >= _depth:
            return False
        if _pit[y+1][x]:
            return False
        
    return True

def spawn_rock(xy):
    return [2+xy[0],highest-3-xy[1]]

rocks = []
rocks.append([[0,0],[1,0],[2,0],[3,0]]) # Line
rocks.append([[0,1],[1,0],[1,1],[1,2],[2,1]]) # Plus
rocks.append([[0,0],[1,0],[2,0],[2,1],[2,2]]) # L
rocks.append([[0,0],[0,1],[0,2],[0,3]]) # Pipe
rocks.append([[0,0],[1,0],[0,1],[1,1]]) # Cube

chamber = [] # for falling rock coords
pit = [] # for staic rocks
highest = 0 # highest from top
depth = 0 #lenght of pit so it doesn't need to be calculated

for i in range(6-highest):
    pit.insert(0,[False,False,False,False,False,False,False])
    depth += 1
    
instruction = ""
with open("2022\\17\\input.txt","r") as f:
    instruction = f.readline().strip()

ins_pos = 0
rock_pos = 0
rock_count = 0
l_i = len(instruction)
l_r = len(rocks)
spawn = False
r = 1000000000000 #2022

# only first rock spawn 
highest = len(pit)-1
for x,y in rocks[rock_pos]:
    chamber.append([2+x,highest-3-y])

rock_pos += 1
rock_count += 1

while rock_count <= r:
    if ins_pos >= l_i:
        ins_pos = 0
    if rock_pos >= l_r:
        rock_pos = 0

    # spawn rock
    if spawn:
        # transfer chamber to pit
        for x,y in chamber:
            pit[y][x] = True
            # find if it is highest
            if y-1 < highest:
                highest = y-1
        
        # pit expansion
        for i in range(6-highest):
            pit.insert(0,[False,False,False,False,False,False,False])
            highest +=1
            depth += 1

        # spawn a rock into chamber
        chamber = list(map(spawn_rock,rocks[rock_pos]))

        # update
        rock_pos += 1
        rock_count += 1
        spawn = False
        """
        for i in pit:
            for j in i:
                if j:
                    print(1,end=" ")
                else:
                    print(0,end=" ")
            print()"""
    # movement based on instruction
    if instruction[ins_pos] == "<" and left(chamber,pit):
        for pos in chamber:
            pos[0] -= 1
    elif instruction[ins_pos] == ">" and right(chamber,pit):
        for pos in chamber:
            pos[0] += 1
    ins_pos += 1

    # movement down
    if down(chamber,pit,depth):
        for pos in chamber:
            pos[1] += 1

    # new rock
    else:
        spawn = True

for i,level in enumerate(pit):
    if True in level:
        print("Highest point in the pit:", depth-i)
        break
print(time.time()-timer)