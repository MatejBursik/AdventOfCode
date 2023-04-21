"""
[T] [V]                     [W]    
[V] [C] [P] [D]             [B]    
[J] [P] [R] [N] [B]         [Z]    
[W] [Q] [D] [M] [T]     [L] [T]    
[N] [J] [H] [B] [P] [T] [P] [L]    
[R] [D] [F] [P] [R] [P] [R] [S] [G]
[M] [W] [J] [R] [V] [B] [J] [C] [S]
[S] [B] [B] [F] [H] [C] [B] [N] [L]
 1   2   3   4   5   6   7   8   9 
"""

def move(_num,_from,_to):
    _array = []
    for i in range(int(_num)):
        _String = "_array.append(l" + _from + ".pop())"
        eval(_String)
    _array.reverse()
    _String2 = "l" + _to + ".extend(_array)"
    eval(_String2)
    
l1 = ["s","m","r","n","w","j","v","t"]
l2 = ["b","w","d","j","q","p","c","v"]
l3 = ["b","j","f","h","d","r","p"]
l4 = ["f","r","p","b","m","n","d"]
l5 = ["h","v","r","p","t","b"]
l6 = ["c","b","p","t"]
l7 = ["b","j","r","p","l"]
l8 = ["n","c","s","l","t","z","b","w"]
l9 = ["l","s","g"]

with open("AdventOfCode\\2022\\05\\input.txt") as f:
    for line in f:
        data = line.strip().split(" ")
        data.pop(0); data.pop(1); data.pop(2) #structure number=[0] from=[1] to=[2]

        move(data[0],data[1],data[2])
        
    var1 = l1[len(l1)-1] + l2[len(l2)-1] + l3[len(l3)-1] + l4[len(l4)-1] + l5[len(l5)-1] + l6[len(l6)-1] + l7[len(l7)-1] + l8[len(l8)-1] + l9[len(l9)-1]
    print(var1.upper())
