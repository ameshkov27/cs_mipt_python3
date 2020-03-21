from graph import *
from numpy import cos, sin, pi


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


def sky():
    brushColor(135, 206, 235)
    penColor(135, 206, 235)
    rectangle(0, 0, 500, 200)


def sea():
    brushColor('blue')
    penColor('blue')
    rectangle(0, 200, 500, 350)


def waves():
    x = 25
    for i in range(500 // 2 * 50):
        if i % 2 == 0:
            brushColor('blue')
            penColor('blue')
            circle(x, 320, 50)

        else:
            brushColor('yellow')
            penColor('yellow')
            circle(x, 380, 50)
        x += 50 * 1.6


def beach():
    brushColor('yellow')
    penColor('yellow')
    rectangle(0, 350, 500, 600)


def sun(x, y, r):
    penColor('yellow')
    brushColor('yellow')

    def pol2dec(r: float, phi: float) -> tuple:
        x = r * cos(phi) + 400
        y = r * sin(phi) + 100
        point = (x, y)
        return point

    l = []
    VERTEX_NUM_MIN, VERTEX_NUM_MAX = 1, 90
    radius, RADIUS_INC = 40, 20
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


def boat(x, y):
    penColor('black')
    brushColor(210, 105, 30)
    circle(x - 60, y, 30)

    penColor('blue')
    brushColor('blue')
    rectangle(0, 200, x, y)

    penColor('black')
    brushColor(255, 228, 181)
    penSize(1)
    polygon([(x + 3, y - 100), (x + 15, y - 50), (x + 60, y - 50), (x + 3, y - 100)])
    polygon([(x + 3, y), (x + 15, y - 50), (x + 60, y - 50), (x + 3, y)])
    penSize(7)
    line(x, y, x, y - 100)

    brushColor(210, 105, 30)
    penSize(0.5)
    rectangle(x - 60, y, x + 100, y + 30)
    polygon([(x + 100, y + 30), (x + 100, y), (x + 180, y), (x + 180, y)])

    brushColor('black')
    circle(x + 112, y + 11, 8)
    brushColor('white')
    circle(x + 112, y + 11, 5)


def small_boat(x, y):
    brushColor(210, 105, 30)
    penSize(1)
    circle(x - 30, y, 20)

    penColor('blue')
    brushColor('blue')
    rectangle(x, y, x - 50, y - 20)

    penColor('black')
    brushColor(210, 105, 30)
    penSize(1)
    rectangle(x - 30, y, x + 50, y + 20)
    polygon([(x + 50, y), (x + 50, y + 20), (x + 90, y), (x + 50, y)])

    penColor('black')
    brushColor(255, 228, 181)
    polygon([(x + 2, y - 72), (x + 10, y - 35), (x + 30, y - 35), (x + 2, y - 70)])
    polygon([(x + 2, y), (x + 10, y - 35), (x + 30, y - 35), (x + 2, y)])

    penColor('black')
    penSize(5)
    line(x, y, x, y - 70)

    penSize(1)
    brushColor('black')
    circle(x + 57, y + 8, 4)
    brushColor('white')
    circle(x + 57, y + 8, 3)


def umbrella(x, y):
    penColor('orange')
    penSize(7)
    line(x, y, x, y + 150)

    penColor('black')
    penSize(1)
    brushColor(255, 99, 71)
    polygon([(x, y), (x - 70, y + 40), (x + 70, y + 40), (x, y)])

    penColor('black')
    penSize(1)
    k = 60
    for i in range(6):
        line(x, y, x - k, y + 40)
        line(x, y, x + k, y + 40)
        k -= 10


def small_umbrella(x, y):
    penColor('orange')
    penSize(5)
    line(x, y, x, y + 100)

    penColor('black')
    penSize(1)
    brushColor(255, 99, 71)
    polygon([(x, y), (x - 40, y + 30), (x + 40, y + 30), (x, y)])
    k = 30
    for i in range(6):
        line(x, y, x - k, y + 30)
        line(x, y, x + k, y + 30)
        k -= 10


sky()
beach()
sea()
waves()
cloud(20, 55, 55)
cloud(10, 300, 65)
cloud(15, 190, 130)
sun(400, 80, 40)
boat(300, 230)
small_boat(70, 220)
x = 200
y = 200
umbrella(80, 300)
small_umbrella(300, 350)

run()
