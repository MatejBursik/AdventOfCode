rules = []
elements = {}
posibilities = {}
Chemical = ""

with open("AdventOfCode\\2021\\14\\input.txt","r") as f:
    Chemical = f.readline().strip()
    f.readline()
    for line in f:
        rules.append(line.strip().split(" -> "))
        

#setting up dictionaty
for term in rules:
    posibilities.update({term[0]:0})

#count the posibilities in the first chemical
count = 1
term = ""

for term in rules:
    elements.update({term[1]:0})

for i in Chemical:
    if count ==  len(Chemical):
        break
    term = i + Chemical[count]
    x = posibilities[term]
    posibilities.update({term: int(x) + 1})

    elements[i] += 1

    count += 1
elements[Chemical[count-1]] += 1

#updating posibilities
def polymerization():
    global posibilities
    new = {}
    for term in rules:
        new.update({term[0]:0})
    for t1,t2 in rules:
        new[t1[0]+t2] += posibilities[t1]
        new[t2+t1[1]] += posibilities[t1]
        elements[t2] += posibilities[t1]
    posibilities = new
    
for i in range(40):
    polymerization()

print(max(elements.values())-min(elements.values()))