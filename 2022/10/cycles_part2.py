"""
addx V - takes two cycles to complete. the X register is increased by the value V. (V can be negative.)
noop - takes one cycle to complete. It has no other effect.
"""

def check():
    pos = [X_register - 1, X_register, X_register + 1]
    if (len(crt)%40) in pos:
        return "#"
    else:
        return "."

with open("AdventOfCode\\2022\\10\\input.txt","r") as f:
    X_register = 1
    cycles = 0
    crt = []
    for line in f:
        line = line.strip()
        if line == "noop":
            cycles += 1
            crt.append(check())
        else:
            line = line.split(" ")
            for i in range(2):
                cycles += 1
                crt.append(check())
            X_register += int(line[1])

with open("AdventOfCode\\2022\\10\\output.txt","w") as f:
    for i,pix in enumerate(crt):
        if i%40 == 0:
            f.write("\n")
            f.write(pix)
        else:
            f.write(pix)