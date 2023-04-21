#input = numebr of calories in a snack, empty line separates elves 

with open("AdventOfCode\\2022\\01\\input.txt") as f:
    elves_calories = []
    carry = []
    for line in f:
        line = line.strip()
        if line == "":
            elves_calories.append(sum(carry))
            carry = []
            continue
        carry.append(int(line))
elves_calories = sorted(elves_calories, reverse=True)
print(elves_calories[0])
print(elves_calories[0] + elves_calories[1] + elves_calories[2])
