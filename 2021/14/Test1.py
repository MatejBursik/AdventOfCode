rules = {}
hold = []
Polymers = []
posibilities = {}
Chemical = ""

with open("AdventOfCode\\14\\input.txt","r") as f:
    for line in f:
        if len(line.replace("\n","")) == 7:
            rules.update({line[:2]: [line[0] + line[6:7], line[6:7] + line[1]]})
        else:
            hold.append(line)            
    Chemical = str(hold[0])

#setting up dictionaty
for term in rules:
    posibilities.update({term[0]:0})

#count the posibilities in the first chemical
count = 1
term = ""
for i in Chemical:
    if count ==  len(Chemical):
        break
    term = i + Chemical[count]
    x = posibilities[term]
    posibilities.update({term, x + 1})
    
#updating posibilities
def polymerization():
    for key in posibilities:
        x = posibilities[key]
        posibilities.update({key, 0})
        posibilities.update({rules[key[0]]: posibilities[rules[key[0]]] + x})
        posibilities.update({rules[key[1]]: posibilities[rules[key[1]]] + x})
    
for i in range(10):
    polymerization()
print(posibilities)

TOTaL = 0
for x in posibilities.values():
    TOTaL += int(x)

print(x)