"""
- part 1
rock = A , X , points = 1
paper = B , Y , points = 2
scissors = C , Z , points = 3

win = 6, draw = 3, lost = 0
point per rount = outcome + what you used
"""

#part1
with open("AdventOfCode\\2022\\02\\input.txt") as f:
    points = 0
    for game in f:
        elf, you = game.strip().split(" ")
        if elf == "A" and you == "Y":
            points += 2 + 6
        elif elf == "A" and you == "Z":
            points += 3 + 0
        elif elf == "A" and you == "X":
            points += 1 + 3
        elif elf == "B" and you == "Y":
            points += 2 + 3
        elif elf == "B" and you == "Z":
            points += 3 + 6
        elif elf == "B" and you == "X":
            points += 1 + 0
        elif elf == "C" and you == "Y":
            points += 2 + 0
        elif elf == "C" and you == "Z":
            points += 3 + 3
        elif elf == "C" and you == "X":
            points += 1 + 6
print(points)

"""
- part 2
X = need to lose
Y = need to draw
Z = need to win
"""

#part2
with open("AdventOfCode\\2022\\02\\input.txt") as f:
    points = 0
    for game in f:
        elf, outcome = game.strip().split(" ")
        if elf == "A" and outcome == "Y":
            points += 1 + 3
        elif elf == "A" and outcome == "Z":
            points += 2 + 6
        elif elf == "A" and outcome == "X":
            points += 3 + 0
        elif elf == "B" and outcome == "Y":
            points += 2 + 3
        elif elf == "B" and outcome == "Z":
            points += 3 + 6
        elif elf == "B" and outcome == "X":
            points += 1 + 0
        elif elf == "C" and outcome == "Y":
            points += 3 + 3
        elif elf == "C" and outcome == "Z":
            points += 1 + 6
        elif elf == "C" and outcome == "X":
            points += 2 + 0
print(points)
