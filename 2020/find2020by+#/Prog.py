with open("AdventOfCode\\2020\\find2020by+#\\Numbers.txt","r") as f:
    um = []
    for num in f:
        um.append(int(num.strip()))
    
    """ for i in um:
        for o in um:
            for p in um:
                if (i+o+p == 2020):
                    print(i,o,p) """
    
    done = False
    for i in range(0,len(um)):
        for o in range(i+1,len(um)):
            for p in range(o+1,len(um)):
                if (um[i]+um[o]+um[p] == 2020):
                    print(um[i],um[o],um[p])
                    done = True
                    break
            if done:
                break
        if done:
            break

