from math import lcm

class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.divide = 1
        self.true = 1
        self.false = 1
        self.inspections = 0

    def test(self, num):
        return num % self.divide == 0


with open("AdventOfCode\\2022\\11\\input.txt") as f:
    data = []
    for line in f:
        data.append(line.strip())

monkeys = []
for line in data:
    line = line.strip()
    
    if line.startswith("Monkey"):
        monkeys.append(Monkey())

    elif line.startswith("Starting"):
        items = [int(x) for x in line.split(": ")[1].split(", ")]
        monkeys[-1].items = items

    elif line.startswith("Operation"):
        operation = line.split(": ")[1].split(" = ")[1]
        monkeys[-1].operation = eval("lambda old:" + operation)

    elif line.startswith("Test"):
        monkeys[-1].divide = int(line.split(" ")[-1])

    elif line.startswith("If true"):
        monkeys[-1].true = int(line.split(" ")[-1])

    elif line.startswith("If false"):
        monkeys[-1].false = int(line.split(" ")[-1])

modulus = lcm(*[m.divide for m in monkeys])
for i in range(10_000):
    for monke in monkeys:
        while len(monke.items) > 0:
            item = monke.items.pop(0)
            new = monke.operation(item)
            new = new % modulus
            if monke.test(new):
                throw_to = monke.true
            else:
                throw_to = monke.false
            
            monkeys[throw_to].items.append(new)
            monke.inspections += 1

inspections = sorted([monke.inspections for monke in monkeys],reverse=True)
print(inspections[0] * inspections[1])
