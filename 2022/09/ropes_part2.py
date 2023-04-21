def move(_head,_tail):
    if abs(_head[0] - _tail[0]) <= 1 and abs(_head[1] - _tail[1]) <= 1:
        return _tail
    
    if _head[0] - _tail[0] > 0: #down
        _tail[0] += 1
    elif _head[0] - _tail[0] < 0: #up
        _tail[0] -= 1

    if _head[1] - _tail[1] > 0: #right
        _tail[1] += 1
    elif _head[1] - _tail[1] < 0: #left
        _tail[1] -= 1

    return _tail


tail_length = 9 + 1 #number of tail parts + head

with open("AdventOfCode\\2022\\09\\input.txt") as f:
    tails = [[0,0] for i in range(tail_length)]
    visited = []
    for line in f:
        line = line.strip().split(' ')
        for num in range(int(line[1])):
            #move head
            head = tails[0] #first tail is the head
            if line[0] == "U":
                head[0] -= 1 #up
            elif line[0] == "D":
                head[0] += 1 #down
            elif line[0] == "R":
                head[1] += 1 #right
            elif line[0] == "L":
                head[1] -= 1 #left
            
            #move tail
            for i in range(1,tail_length):
                tails[i] = move(tails[i - 1],tails[i])
            
            visited.append(str(tails[-1])) #getting only the last tail

print(len(set(visited)))
