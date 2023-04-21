playersPos = []
playerScore = [0,0]
dice = 0
count = 0

with open("AdventOfCode\\2021\\21\\input.txt","r") as f:
    for player in f:
        playersPos.append(int(player.split(": ")[1].strip("\n")))

def roll(Score):
    global dice, count, playersPos, Pos
    for q in range(3):
        dice += 1
        count += 1
        if dice == 101:
            dice = 1
        for i in range(dice):
            playersPos[Pos] += 1
            if playersPos[Pos] == 11:
                playersPos[Pos] = 1
    
    Score = playersPos[Pos]

    return(Score)

finish = False
while finish == False:
    Pos = 0
    playerScore[0] += roll(playerScore[0])
    if 1000 == playerScore[0]:
        break
    Pos = 1
    playerScore[1] += roll(playerScore[1])
    if 1000 == playerScore[1]:
        break

print(playerScore[1]*count)

