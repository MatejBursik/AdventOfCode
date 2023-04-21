maps = []

with open("AdventOfCode\\2022\\08\\input.txt") as f:
    for y in f:
        y = y.strip()
        y_collector = []
        for x in y:
            y_collector.append(int(x))
        maps.append(y_collector)

#searching for highest score of the best scenic tree
"""
measure the viewing distance from a given tree
look (up, down, left, right) from that tree
stop if you reach an edge or at the first tree that is the same height or taller
include the stopping tree while counting
If a tree is right on the edge, at least one of its viewing distances will be 0
"""

score = 0 #multiply all distances

def looking(y_pos, x_pos, height):
    global maps
    _scores = [0,0,0,0] #left,right,up,down

    for x in range(x_pos)[::-1]: #left
        _scores[0] += 1
        if height <= maps[y_pos][x]:
            break

    for x in range(len(maps[0])-x_pos-1): #right
        x += x_pos
        _scores[1] += 1
        if height <= maps[y_pos][x+1]:
            break

    for y in range(y_pos)[::-1]: #up
        _scores[2] += 1
        if height <= maps[y][x_pos]:
            break

    for y in range(len(maps)-y_pos-1): #down
        y += y_pos
        _scores[3] += 1
        if height <= maps[y+1][x_pos]:
            break

    return _scores[0]*_scores[1]*_scores[2]*_scores[3]


for y,yd in enumerate(maps[1:-1]):
        y += 1 #shift he value by limiter in for cicle because enumerate does range not index
        for x,xd in enumerate(yd[1:-1]):
            x += 1 #shift he value by limiter in for cicle because enumerate does range not index
            hold = looking(y,x,xd)
            if hold > score:
                score = hold

print(score)
