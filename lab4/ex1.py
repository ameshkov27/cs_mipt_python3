from graph import *
from math import cos, sin, radians, pi


def main():
    sky()
    sea()
    beach()
    sun(400, 100, 40)
    cloud(25, 55, 55)
    cloud(10, 300, 65)
    cloud(15, 190, 130)
    waves()
    boat(300, 280, 8)
    boat(100, 220, 5)
    umbrella(80, 300, 7)
    umbrella(300, 380, 5)


def sky():
    brushColor(135, 206, 235)
    penColor(135, 206, 235)
    rectangle(0, 0, 500, 200)


def sea():
    brushColor(123, 104, 238)
    penColor(123, 104, 238)
    rectangle(0, 200, 500, 200 + 350)


def beach():
    brushColor('yellow')
    penColor('yellow')
    rectangle(0, 350, 500, 600)


def sun(x_cord, y_cord, size):
    penColor('yellow')
    brushColor('yellow')

    def pol2dec(r: float, phi: float) -> tuple:
        x = r * cos(phi) + x_cord
        y = r * sin(phi) + y_cord
        point = (x, y)
        return point

    l = []
    VERTEX_NUM_MIN, VERTEX_NUM_MAX = 1, 90
    radius, RADIUS_INC = size, 20
    angle, ANGLE_INC = 0, 2 * pi / VERTEX_NUM_MAX
    moveTo(*pol2dec(radius, angle))
    for vc in range(VERTEX_NUM_MIN, VERTEX_NUM_MAX // 2 + 1):
        radius += RADIUS_INC
        angle += ANGLE_INC
        l.append(pol2dec(radius, angle))
        radius -= RADIUS_INC
        angle += ANGLE_INC
        l.append(pol2dec(radius, angle))
    polygon(l)


def cloud(r, x, y):
    penColor('white')
    brushColor('white')
    circle(x, y, r)
    circle(x + 1.2 * r, y, r)
    circle(x + 2.4 * r, y, r)
    circle(x + 3 * r, y + r, r)
    circle(x + 2 * r, y + r, r)
    circle(x + 1 * r, y + r, r)
    circle(x - 0.4 * r, y + r, r)


def waves():
    x = 25
    for i in range(500 // 2 * 50):
        if i % 2 == 0:
            brushColor(123, 104, 238)
            penColor(123, 104, 238)
            circle(x, 320, 50)

        else:
            brushColor('yellow')
            penColor('yellow')
            circle(x, 380, 50)
        x += 50 * 1.6


def boat(x, y, size):
    penSize(1)
    penColor('black')
    brushColor(210, 105, 30)
    rectangle(x - 9 * size, y, x + size * 14, y + size * 3.5)

    penColor('black')
    penSize(size)
    line(x, y, x, y - size * 14)

    penColor('black')
    penSize(0)
    polygon([(x + size * 14, y + size * 3.5), (x + size * 14, y), (x + size * 23, y), (x + size * 14, y + size * 3.5)])

    brushColor(210, 105, 30)
    mylist = []
    for i in range(91):
        pointX = cos(radians(90 + i)) * size * 3.6
        pointY = sin(radians(90 + i)) * size * 3.6
        pointX, pointY = pointX + x - 9 * size, pointY + y
        mylist.append((pointX, pointY))
    mylist.append((x - 9 * size, y))
    polygon(mylist)

    penColor('black')
    brushColor(255, 228, 181)
    penSize(1)
    polygon([(x + 0.5 * size, y - size * 14), (x + 2 * size, y - size * 7), (x + size * 9, y - size * 7),
             (x + 0.5 * size, y - size * 14)])
    polygon([(x + 0.5 * size, y), (x + 2 * size, y - size * 7), (x + size * 9, y - size * 7), (x + 0.5 * size, y)])

    brushColor('black')
    penColor('black')
    penSize(0.1)
    circle(x + size * 16, y + size * 1.4, size)
    brushColor('white')
    penColor('white')
    circle(x + size * 16, y + size * 1.4, size * 0.6)


def umbrella(x, y, size):
    penColor('orange')
    penSize(size)
    line(x, y, x, y + size * 20)

    penColor('black')
    penSize(1)
    brushColor(255, 99, 71)
    polygon([(x, y), (x - size * 10, y + size * 5), (x + size * 10, y + size * 5), (x, y)])

    penColor('black')
    penSize(1)

    for i in range(0, size * 10, size * 2):
        line(x, y, x + i, y + size * 5)
        line(x, y, x - i, y + size * 5)


if __name__ == "__main__":
    main()
    run()
