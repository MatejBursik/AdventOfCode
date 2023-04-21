with open("AdventOfCode\\2021\\8\\input.txt") as f:
    data = []
    what = {}
    total = 0
    for line in f:
        data.append([line.strip().split(" | ")[1].split(" "), line.strip().split(" | ")[0].split(" ")])

    easy_dgits = 0

    def sdigits(inp1,inp2):
        return "".join(set(inp1).intersection(inp2))
    
    for entry in data:
        what = {}
        for string in entry[1]:
            #easy digits (1,7,4,8)
            if len(string) in [2,3,4,7]:
                easy_dgits += 1
                if len(string) == 2:
                    what[1] = "".join(sorted(string))
                elif len(string) == 3:
                    what[7] = "".join(sorted(string))
                elif len(string) == 4:
                    what[4] = "".join(sorted(string))
                else:
                    what[8] = "".join(sorted(string))
    
        for string1 in entry[1]:
            if len(string1) not in [2,3,4,7]:
                #comparisosn of six string digits
                if len(string1) == 5:
                    if len(sdigits(string1,what.get(7))) == 3:
                        what[3] = "".join(sorted(string1))
                    elif len(sdigits(string1,what.get(4))) == 3:
                        what[5] = "".join(sorted(string1))
                    else:
                        what[2] = "".join(sorted(string1))
                #comparison of five string digits
                else:
                    if len(sdigits(string1,what.get(4))) == 4:
                        what[9] = "".join(sorted(string1))
                    elif len(sdigits(string1,what.get(1))) == 2:
                        what[0] = "".join(sorted(string1))
                    else:
                        what[6] = "".join(sorted(string1))

        temp_total = ""

        #adding the value of the right side of the input to the tatal
        for beep in entry[0]:
            for i in range(0,10):
                if what.get(i) == "".join(sorted(beep)):
                    temp_total = temp_total + str(i)
        
        total += int(temp_total)

    print(total)