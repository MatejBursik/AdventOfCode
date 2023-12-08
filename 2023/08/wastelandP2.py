from math import lcm

network = dict()
ghosts = []
steps = 0
with open("2023\\08\\input.txt","r") as f:
    instruction = f.readline().strip()
    f.readline()
    for line in f:
        destination,lf = line.strip().split(" = ")
        network[destination] = lf[1:-1].split(", ")

for key in network.keys():
    if key[-1] == "A":
        ghosts.append(key)

count = 0
insLen = len(instruction)
results = []
for pos in ghosts:
    steps = 0
    while "Z" not in pos:
        if instruction[count] == "L":
            pos = network[pos][0]
        elif instruction[count] == "R":
            pos = network[pos][1]
        steps += 1
        count += 1
        if count >= insLen:
            count = 0
    results.append(steps)

print(lcm(*results))