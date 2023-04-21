with open("AdventOfCode\\2022\\09\\input.txt") as f:
    head = [0,0]; tail = [0,0]
    tail_positions = {(0, 0)}
    for line in f:
        line = line.strip().split(" ")

        for i in range(int(line[1])):
            #move head
            if line[0] == "U":
                head[0] -= 1
                
            elif line[0] == "D":
                head[0] += 1
                
            elif line[0] == "L":
                head[1] -= 1

            elif line[0] == "R":
                head[1] += 1

            #move tail
            if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1: 
                diff = [head[0]-tail[0],head[1]-tail[1]]
                if diff[0] == 2:
                    tail[0] += 1
                    if diff[1] == 1: #diagonal
                        tail[1] += 1
                    elif diff[1] == -1:
                        tail[1] -= 1

                elif diff[0] == -2:
                    tail[0] -= 1
                    if diff[1] == 1: #diagonal
                        tail[1] += 1
                    elif diff[1] == -1:
                        tail[1] -= 1

                elif diff[1] == 2:
                    tail[1] += 1
                    if diff[0] == 1: #diagonal
                        tail[0] += 1
                    elif diff[0] == -1:
                        tail[0] -= 1

                elif diff[1] == -2:
                    tail[1] -= 1
                    if diff[0] == 1: #diagonal
                        tail[0] += 1
                    elif diff[0] == -1:
                        tail[0] -= 1

                tail_positions.add(tuple(tail))
        
print(len(tail_positions)) #number of places tail visited
