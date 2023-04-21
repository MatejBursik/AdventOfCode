Input = []

with open("AdventOfCode\\2021\\3\\input.txt","r") as f:
    for l in f:
        carry = l.replace("\n","")
        Input.append(carry)

#Part1
gammas = []
gamma = ""
epsilon = ""

for count in range(len(Input[0])):
    for data in Input:
        gammas.append(data[count])
    O = int(gammas.count("0"))
    L = int(gammas.count("1"))
    if O < L:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    gammas.clear()
print(gamma,epsilon)
power = int(gamma,2)*int(epsilon,2)
print(power)

#Part2

#MostCommon
import testh
#LeastCommon
import test as test

lifeSupportRating = int(test.CO2scrubber,2)*int(testh.oxygenGenRating,2)
print(lifeSupportRating)