Input = []

with open("AdventOfCode\\2021\\24\\input.txt","r") as f:
    for line in f:
        Input.append(line.strip().split(" "))

Executable = []
line = ""

for l in Input:
    if len(l)==3:
        line = l[1]+"="+l[0]+"("+l[1]+","+l[2]+")"
    else:
        line = l[0]+"("+l[1]+")"
    Executable.append(line)

dNumber = "99999999999999"
y = 0
z = 0
x = 0
w = 0

def inp(var):
    global dNumber
    global y,z,x,w
    w = int(dNumber[0])
    dNumber = dNumber[1:]

def add(var1,var2):
    hold = var1 + var2
    return(hold)


def mul(var1,var2):
    hold = var1 * var2
    return(hold)

def div(var1,var2):
    hold = round(var1 / var2)
    return(hold)

def mod(var1,var2):
    hold = var1 % var2
    return(hold)

def eql(var1,var2):
    if var1 == var2:
        return(1)
    else:
        return(0)

count = 11415882
run = True
while run:
    y = 0
    z = 0
    x = 0
    w = 0
    for Command in Executable:
        exec(Command)
    if z == 0:
        run = False
    else:
        dNumber = "99999999999999"
        count += 1
        dNumber = str(int(dNumber) - count)
        while "0" in dNumber:
            count += 1
            dNumber = str(int(dNumber) - count)

print(dNumber)

""" 
so far count: 11415882
99999999999999 > x > 88888888888888


input number is a serial number (14 digit long)
we need to find the highest serial number were at the end (z = 0)

inp(var) = read input from var
add(var1 var2) = adds var1 to var2 and saves it in var1 
mul(var1 var2) = multiplys var1 by var2 and saves it in var1
div(var1 var2) = divides var1 by var2 and saves it in int(var1)
mod(var1 var2) = modlo var1 by var2 and saves it in var1
eql(var1 var2) = if values var1 and var2 are equal var1 = 1, if not var1 = 0

var1 = w,x,y,z
var2 = var1 or number """
