binInput = []
with open("AdventOfCode\\2021\\16\\test.txt","r") as f:
    for Intp in f:
        for hex in Intp:
            Bin = bin(int(hex.replace("A","10").replace("B","11").replace("C","12").replace("D","13").replace("E","14").replace("F","15"))).replace("0b","")
            binInput.append((4-len(Bin))*"0" + Bin)

code = ""
for x in binInput:
    code = code + x

oldCode = code
totalVersion = 0
#print(code)


def Starter(code):
    t = code[3]+code[4]+code[5]
    i = code[6]
    Type = int(t,2) + 1
    if Type == 4:
        code = literal(code)
    elif i == "0":
        code = operate0(code)
    elif i == "1":
        code = operate1(code)
    return code


def literal(code):
    global totalVersion
    v = ""
    t = "" #how many bits are for packet +1 at the begining to determin end
    Version = 0
    Type = 0
    packets = []
    counter = 0

    v = code[0]+code[1]+code[2]
    t = code[3]+code[4]+code[5]
    code = code[6:]
    Version = int(v,2)
    Type = int(t,2) + 1
    counter += 6
    totalVersion += Version

    #creating packets
    while code[0] == "1":
        packets.append(code[1:(Type)])
        code = code[Type:]
        counter += 5
    packets.append(code[1:(Type)])
    code = code[Type:]
    counter += 5

    #deleting 0s
    code = code[((4-(counter%4))%4):]

    return(code)


def operate0(code):
    global totalVersion
    
    v = ""
    t = "" #how many bits are for packet +1 at the begining to determin end
    Type = 0
    packets = []
    counter = 0
    v = code[0]+code[1]+code[2]
    Version = int(v,2)
    totalVersion += Version
    code = code[7:]
    L = int(code[:15],2)

    code = code[15:]
    counter += 22

    TOTALpacketL = 0

    while TOTALpacketL < L:
        v = code[0]+code[1]+code[2]
        t = code[3]+code[4]+code[5]
        code = code[6:]
        Version = int(v,2)
        Type = int(t,2) + 1
        counter += 6
        TOTALpacketL += 6
        totalVersion += Version

        #creating packets
        while code[0] == "1":
            packets.append(code[1:(Type)])
            code = code[Type:]
            counter += 5
            TOTALpacketL += 5
        packets.append(code[1:(Type)])
        code = code[Type:]
        counter += 5
        TOTALpacketL += 5
   
    #deleting 0s
    code = code[(((4-(counter%4))%4)+4):]

    return(code)


def operate1(code):
    global totalVersion
    
    return(code)


while len(code) != 0:
    code = Starter(code)
    print("running")
print(totalVersion)
