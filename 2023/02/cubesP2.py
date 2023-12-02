with open("2023\\02\\input.txt", "r") as f:
    gameIds = 0
    for i,game in enumerate(f):
        game = game.strip().split(": ")[1]
        sets = game.strip().split("; ")
        red = 0
        green = 0
        blue = 0
        for sub in sets:
            sub = sub.strip().split(", ")
            for color in sub:
                color = color.strip().split(" ")
                match color[1]:
                    case "red":
                        if int(color[0])>red:
                            red = int(color[0])
                    case "green":
                        if int(color[0])>green:
                            green = int(color[0])
                    case "blue":
                        if int(color[0])>blue:
                            blue = int(color[0])        
        gameIds += (red*green*blue)

    print(gameIds)