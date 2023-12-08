def sort_hands(old_hands, new_h):
    for i,old_h in enumerate(old_hands):
        for card in zip(old_h[0],new_h[0]):
            if card[0] > card[1]:
                return i
            if card[0] < card[1]:
                break
    return len(old_hands)

kinds = {
    "five_kind":[],
    "four_kind":[],
    "house":[],
    "three_kind":[],
    "two_pair":[],
    "one_pair":[],
    "highest":[]
}
maxRank = 0
sort_key = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
with open("2023\\07\\input.txt","r") as f:
    for line in f:
        maxRank += 1
        hand = dict()
        line = line.strip().split(" ")

        for card in line[0]:
            if card in hand.keys():
                hand[card] += 1
            else:
                hand[card] = 1

        if "J" in hand.keys():
            # change Js in hand to the ather highest key
            print(hand.keys())
            highest = ["",0]
            j = hand["J"]
            hand.pop("J")
            for key in hand.keys():
                if hand[key] > highest[1]:
                    highest = [key, hand[key]]
                elif hand[key] == highest[1]:
                    if sort_key.index(key) < sort_key.index(highest[0]):
                        highest = [key, hand[key]]
            if highest == ["",0]:
                hand[sort_key[0]] = j
            else:
                hand[highest[0]] += j
            
        if len(hand) == 1:
            new_hand = [[sort_key.index(c) for c in line[0]], line[1]]
            if len(kinds["five_kind"]) != 0:
                kinds["five_kind"].insert(sort_hands(kinds["five_kind"],new_hand), new_hand)
            else:
                kinds["five_kind"].append(new_hand)
            
        elif len(hand) == 2:
            if sorted(list(hand.values())) == [1,4]:
                new_hand = [[sort_key.index(c) for c in line[0]], line[1]]
                if len(kinds["four_kind"]) != 0:
                    kinds["four_kind"].insert(sort_hands(kinds["four_kind"],new_hand), new_hand)
                else:
                    kinds["four_kind"].append(new_hand)

            elif sorted(list(hand.values())) == [2,3]:
                new_hand = [[sort_key.index(c) for c in line[0]], line[1]]
                if len(kinds["house"]) != 0:
                    kinds["house"].insert(sort_hands(kinds["house"],new_hand), new_hand)
                else:
                    kinds["house"].append(new_hand)

        elif len(hand) == 3:
            if sorted(list(hand.values())) == [1,1,3]:
                new_hand = [[sort_key.index(c) for c in line[0]], line[1]]
                if len(kinds["three_kind"]) != 0:
                    kinds["three_kind"].insert(sort_hands(kinds["three_kind"],new_hand), new_hand)
                else:
                    kinds["three_kind"].append(new_hand)

            elif sorted(list(hand.values())) == [1,2,2]:
                new_hand = [[sort_key.index(c) for c in line[0]], line[1]]
                if len(kinds["two_pair"]) != 0:
                    kinds["two_pair"].insert(sort_hands(kinds["two_pair"],new_hand), new_hand)
                else:
                    kinds["two_pair"].append(new_hand)

        elif len(hand) == 4:
            new_hand = [[sort_key.index(c) for c in line[0]], line[1]]
            if len(kinds["one_pair"]) != 0:
                kinds["one_pair"].insert(sort_hands(kinds["one_pair"],new_hand), new_hand)
            else:
                kinds["one_pair"].append(new_hand)

        else:
            new_hand = [[sort_key.index(c) for c in line[0]], line[1]]
            if len(kinds["highest"]) != 0:
                kinds["highest"].insert(sort_hands(kinds["highest"],new_hand), new_hand)
            else:
                kinds["highest"].append(new_hand)

total = 0
for key in kinds.keys():
    for _,bid in kinds[key]:
        total += maxRank*int(bid)
        maxRank -= 1

print(total)
