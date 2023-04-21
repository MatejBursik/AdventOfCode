input = []
row = []
height = []

with open("AdventOfCode\\2021\\9\\input.txt","r") as f:
    for l in f:
        input.append(l.split())

    for i in input:
        for x in i:
            for q in x:
                row.append(int(q))
        height.append(row)
        row = []

def get_adjacents(i, j):
    adjacents = []
    if i + 1 < len(height[0]):
        adjacents.append(height[j][i + 1])
    if i - 1 >= 0:
        adjacents.append(height[j][i - 1])
    if j + 1 < len(height):
        adjacents.append(height[j + 1][i])
    if j - 1 >= 0:
        adjacents.append(height[j - 1][i])
    return adjacents
result = 0

for j in range(0, len(height)):
    for i in range(0, len(height[0])):
        if height[j][i] < min(get_adjacents(i, j)):
            result += 1 + height[j][i]

print(result)