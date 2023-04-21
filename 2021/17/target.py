#target area: x=88..125, y=-157..-103

def move(xV,yV):
    posX = 0
    posY = 0
    positions = []

    while (posX < 126 and posY > -158):
        posX += xV
        posY += yV
        positions.append([posX,posY])

        if xV != 0:
            xV -= 1
        yV -= 1

    for x,y in positions:
        if (x < 126 and x > 87 and y < -102 and y > -158):
            return(positions)

yMAX = 0
allANGLES = 0

for x in range(1,200):
    for y in range(-500,500):
        loc = move(x,y)
        if loc != None:
            allANGLES += 1
            for point in loc:
                if point[1] > yMAX:
                    yMAX = point[1]

print(yMAX, allANGLES)
