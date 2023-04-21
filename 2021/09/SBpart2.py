import math
input = []
row = []
height =[]

with open("AdventOfCode\\2021\\9\\input.txt","r") as f:
    for l in f:
        input.append(l.split())

    for i in input:
        for x in i:
            for q in x:
                row.append(int(q))
        height.append(row)
        row = []


groups = []
def count_groups(i, j):
    if j < 0 or j >= len(height) or i < 0 or i >= len(height[0]) or height[j][i] == 9 or height[j][i] == -1:
        return
    height[j][i] = -1
    groups[len(groups)-1] += 1
    count_groups(i+1, j)
    count_groups(i-1, j)
    count_groups(i, j+1)
    count_groups(i, j-1)

for i in range(0, len(height)):
    for j in range(0, len(height[0])):
        groups.append(0)
        count_groups(j, i)
        
print(math.prod(sorted(groups, reverse=True)[:3]))