points = 0
cardsData = []
cards = []
with open("2023\\04\\input.txt", "r") as f:
    for line in f:
        cardsData.append(line)
        cards.append(1) # part 2

for i,card in enumerate(cardsData):
    winning,your = card.strip().split(": ")[1].split(" | ")
    winning = winning.split(" ")
    your = your.split(" ")
    count = 0

    for w in winning:
        for y in your:
            if w.isdigit() and y.isdigit() and w == y:
                count += 1
    
    # part 2
    for idx in range(i+1,i+count+1):
        cards[idx] += cards[i]
    
    # part 1
    if count>0:
        count-=1
        points += 2**count

print("part 1:",points)
print("part 2:",sum(cards))
