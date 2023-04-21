Input = []

with open("AdventOfCode\\3\\input.txt","r") as f:
    for l in f:
        carry = l.replace("\n","")
        Input.append(carry)

gammas = []
oxygenGenRating = ""
CO2scrubber = ""

#MostCommon

count = 0
gammas.clear()


def Repete(NextInput):
    global count, Input, oxygenGenRating
    Mover = []
    if len(NextInput) == 1:
        oxygenGenRating = NextInput[0]
    else:
        for data in NextInput:
            gammas.append(data[count])
        O = int(gammas.count("0"))
        L = int(gammas.count("1"))

        if O < L:
            for data in NextInput:
                if data[count] == "1":
                    Mover.append(data)
        elif O > L:
            for data in NextInput:
                if data[count] == "0":
                    Mover.append(data)
        elif O == L:
            for data in NextInput:
                if data[count] == "1":
                    Mover.append(data)
        else:
            print("FRIDGE")

        gammas.clear()
        NextInput.clear()
        count += 1

        if count == 20:
            Mover.clear()
            Mover.append("FRIDGE")

        Repete(Mover)

Repete(Input)

print(oxygenGenRating)

""" 
Issue
prve opakovanie sa stne ok ale druhe si uz nefeedne ten zostavajuci list do zaciatku definicie 
"""
