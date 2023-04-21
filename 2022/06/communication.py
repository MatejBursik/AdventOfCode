with open("AdventOfCode\\2022\\06\\inut.txt") as file:
    line = file.readline().strip()
    #part1 dist_char=4, part2dist_char=14
    run = True; value = 0; packet = []; dist_char = 14
    for i in range(dist_char):
        packet.append(line[i])
    print(packet)
    line = line[dist_char:]

    if len(set(packet)) == dist_char:
        run = False
    
    while run:
        packet.pop(0)
        packet.append(line[0])
        line = line[1:]
        value += 1
        
        if len(set(packet)) == dist_char:
            run = False

    print(value + dist_char)