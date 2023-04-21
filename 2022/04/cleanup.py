with open("AdventOfCode\\2022\\04\\input.txt") as f:
    number1 = 0
    number2 = 0
    for line in f:
        left, right = line.strip().split(",")
        left = left.split("-")
        right = right.split("-")

        if left[0] == left[1]:
            left = [int(left[0])]
        else:
            left = list(range(int(left[0]),int(left[1])))
            left.append(left[len(left)-1]+1)
        
        if right[0] == right[1]:
            right = [int(right[0])]
        else:
            right = list(range(int(right[0]),int(right[1])))
            right.append(right[len(right)-1]+1)

        #part1
        if left[0] in right and left[len(left)-1] in right:
            number1 += 1
        elif right[0] in left and right[len(right)-1] in left:
            number1 += 1
        #part2
        if set(left) & set(right):
            number2 += 1

    print(number1)
    print(number2)
        