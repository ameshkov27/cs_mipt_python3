from graph import *


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


def beach():
    brushColor('yellow')
    penColor('yellow')
    rectangle(0, 350, 500, 600)


def sun(x, y, r):
    brushColor('yellow')
    penColor('yellow')
    circle(x, y, r)


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


sky()
sea()
beach()
cloud(20, 100, 80)
sun(400, 80, 40)
boat(300, 230)
x = 200
y = 200
umbrella(80, 300)

run()
