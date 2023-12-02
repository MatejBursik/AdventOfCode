with open("2023\\02\\input.txt", "r") as f:
    gameIds = 0
    for i,game in enumerate(f):
        game = game.strip().split(": ")[1]
        sets = game.strip().split("; ")
        playable = True
        for sub in sets:
            red = 0
            green = 0
            blue = 0
            sub = sub.strip().split(", ")
            for color in sub:
                color = color.strip().split(" ")
                match color[1]:
                    case "red":
                        red += int(color[0])
                    case "green":
                        green += int(color[0])
                    case "blue":
                        blue += int(color[0])
            if red>12 or green>13 or blue>14:
                playable = False
        
        if playable:
            gameIds += i+1

    print(gameIds)