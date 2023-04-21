def list_intersection(_lst1, _lst2):
    return list(set(_lst1) & set(_lst2))[0]

def triple_list_intersection(_lst1, _lst2, _lst3):
    return list(set(_lst1) & set(_lst2) & set(_lst3))[0]

def priority(_in):
    _lowerA = "abcdefghijklmnopqrstuvwxyz"
    _upperA = _lowerA.upper()
    if _in.isupper():
        _out = _upperA.index(_in) + 26 + 1
    else:
        _out = _lowerA.index(_in) + 1
    return _out

with open("AdventOfCode\\2022\\03\\input.txt") as f:
    total = 0
    grouptotal = 0
    group = []
    
    for line in f:
        line = line.strip()
        left, right = list(line[:len(line)//2]), list(line[len(line)//2:])
        same = list_intersection(left, right)

        #part1
        total += priority(same)
        
        #part2
        group.append(list(line))
        if len(group) == 3:
            grouptotal += priority(triple_list_intersection(group[0], group[1], group[2]))
            group = []

    print(total)
    print(grouptotal)