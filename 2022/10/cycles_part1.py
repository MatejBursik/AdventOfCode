"""
addx V - takes two cycles to complete. the X register is increased by the value V. (V can be negative.)
noop - takes one cycle to complete. It has no other effect.
"""

def check():
    if cycles in [20,60,100,140,180,220]:
        out = (cycles*X_register)
        return out
    else:
        return 0

with open("AdventOfCode\\2022\\10\\input.txt") as f:
    X_register = 1
    cycles = 0
    out = 0
    for line in f:
        line = line.strip()
        if line == "noop":
            cycles += 1
            out += check()
        else:
            line = line.split(" ")
            for i in range(2):
                cycles += 1
                out += check()
            X_register += int(line[1])

print(out)