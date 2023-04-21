maps = []
visibility = [] #v=visible, h=hidden

with open("AdventOfCode\\2022\\08\\input.txt") as f:
    for y in f:
        y = y.strip()
        y_collector = []
        y_v = []
        for x in y:
            y_collector.append(int(x))
            y_v.append("h")
        maps.append(y_collector)
        visibility.append(y_v)

#setting the outer layers to visible
for i in range(len(visibility[0])):
    visibility[0][i] = "v"
    visibility[-1][i] = "v"

for i in range(len(visibility)-2):
    i += 1
    visibility[i][0] = "v"
    visibility[i][-1] = "v"

#searching for visible trees
"""
search from one side at a time (from:left,right,top,down)
counter for the highest tree from that direction, if 9 is reached stop checking, reset for every line when checking of line
if visible from one side skip continue throught it, but save if it is higher
"""

def replacement_x():
    global visibility
    for y,yd in enumerate(maps[1:-1]):
        y += 1 #shift he value by limiter in for cicle because enumerate does range not index
        value = yd[0]
        for x,xd in enumerate(yd[1:]):
            x += 1 #shift he value by limiter in for cicle because enumerate does range not index
            if value == 9: #no tree is higher than 9
                break
            if visibility[y][x] != "v": #if it is visible, skip-it
                if value < xd:
                    visibility[y][x] = "v"
            if xd > value:
                value = xd

def replacement_y():
    global visibility
    for x in range(len(visibility[0])-2):
        x += 1
        value = maps[0][x]
        for y,yd in enumerate(maps[1:]):
            y = y+1 #shift he value by limiter in for cicle because enumerate does range not index
            if value == 9: #no tree is higher than 9
                break
            if visibility[y][x] != "v": #if it is visible, skip-it
                if value < yd[x]:
                    visibility[y][x] = "v"
            if yd[x] > value:
                value = yd[x]


#left to right
replacement_x()

#right to left - x reversed
for i in range(len(maps)):
    maps[i].reverse()
    visibility[i].reverse()
replacement_x()

#top to bottom
replacement_y()

#bottom to top - y reversed
maps.reverse()
visibility.reverse()
replacement_y()

#counting
counter = 0
for i in visibility:
    counter += i.count("v")
print(counter)
