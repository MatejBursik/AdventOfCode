with open("AdventOfCode\\2021\\8\\input.txt") as inputs:
    ans = sum(len(chars) in (2, 3, 4, 7) for line in inputs for chars in line.split('|')[1].strip().split())
    print("1, 4, 7, or 8 appears: ", ans)