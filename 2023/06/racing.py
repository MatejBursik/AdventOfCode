with open("2023\\06\\input.txt", "r") as f:
    timeD = list(filter(lambda x:x.isdigit(), f.readline().strip().split(": ")[1].split(" ")))
    distanceD = list(filter(lambda x:x.isdigit(),f.readline().strip().split(": ")[1].split(" ")))

print(timeD)
print(distanceD)

# Part 1
p1 = 1
for time,distance in zip(timeD,distanceD):
    waysToWin = []
    for ms in range(int(time)):
        speed = ms
        travel = speed * (int(time)-speed)
        if travel > int(distance):
            waysToWin.append([speed,travel])
    p1 *= len(waysToWin)
print("Part 1:",p1)

# Part 2
time = int("".join(timeD))
distance = int("".join(distanceD))
print(time,distance)

waysToWin = []
for ms in range(time):
    speed = ms
    travel = speed * (time-speed)
    if travel > distance:
        waysToWin.append([speed,travel])
p2 = len(waysToWin)
print("Part 2:",p2)