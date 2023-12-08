network = dict()
pos = "AAA"
end = "ZZZ"
steps = 0
with open("2023\\08\\input.txt","r") as f:
    instruction = f.readline().strip()
    f.readline()
    for line in f:
        destination,lf = line.strip().split(" = ")
        network[destination] = lf[1:-1].split(", ")

count = 0
insLen = len(instruction)
while pos != end:
    if instruction[count] == "L":
        pos = network[pos][0]
    elif instruction[count] == "R":
        pos = network[pos][1]
    steps += 1
    count += 1
    if count >= insLen:
        count = 0


print(steps)