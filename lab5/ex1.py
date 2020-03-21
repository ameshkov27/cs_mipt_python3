from graph import *
from math import cos, sin, radians, pi


def sky():
    brushColor(135, 206, 235)
    penColor(135, 206, 235)
    rectangle(0, 0, 1600, 300)


def sea():
    brushColor(123, 104, 238)
    penColor(123, 104, 238)
    rectangle(0, 300, 1600, 550)


def beach():
    brushColor('yellow')
    penColor('yellow')
    rectangle(0, 550, 1600, 900)


def sun(x_cord, y_cord, size):
    list_obj2 = []
    penColor('yellow')
    brushColor('yellow')

    def pol2dec(r: float, phi: float) -> tuple:
        x = r * cos(phi) + x_cord
        y = r * sin(phi) + y_cord
        point = (x, y)
        return point

    l = []
    VERTEX_NUM_MIN, VERTEX_NUM_MAX = 1, 120
    radius, RADIUS_INC = size, 30
    angle, ANGLE_INC = 0, 2 * pi / VERTEX_NUM_MAX
    moveTo(*pol2dec(radius, angle))
    for vc in range(VERTEX_NUM_MIN, VERTEX_NUM_MAX // 2 + 1):
        radius += RADIUS_INC
        angle += ANGLE_INC
        l.append(pol2dec(radius, angle))
        radius -= RADIUS_INC
        angle += ANGLE_INC
        l.append(pol2dec(radius, angle))
    obj = polygon(l)
    list_obj2.append(obj)
    return list_obj2


def cloud(r, x, y):
    list_obj2 = []
    penColor('white')
    brushColor('white')
    obj = circle(x, y, r)
    list_obj2.append(obj)
    obj = circle(x + 1.2 * r, y, r)
    list_obj2.append(obj)
    obj = circle(x + 2.4 * r, y, r)
    list_obj2.append(obj)
    obj = circle(x + 3 * r, y + r, r)
    list_obj2.append(obj)
    obj = circle(x + 2 * r, y + r, r)
    list_obj2.append(obj)
    obj = circle(x + 1 * r, y + r, r)
    list_obj2.append(obj)
    obj = circle(x - 0.4 * r, y + r, r)
    list_obj2.append(obj)
    return list_obj2


def waves():
    x = 25
    for i in range(500 // 2 * 50):
        if i % 2 == 0:
            brushColor(123, 104, 238)
            penColor(123, 104, 238)
            circle(x, 520, 52)

        else:
            brushColor('yellow')
            penColor('yellow')
            circle(x, 590, 52)
        x += 50 * 1.6


def boat(x, y, size):
    list_obj = []

    penSize(1)
    penColor('black')
    brushColor(210, 105, 30)
    obj = rectangle(x - 9 * size, y, x + size * 14, y + size * 3.5)
    list_obj.append(obj)

    penColor('black')
    penSize(size)
    obj = line(x, y, x, y - size * 14)
    list_obj.append(obj)

    penColor('black')
    penSize(0)
    obj = polygon(
        [(x + size * 14, y + size * 3.5), (x + size * 14, y), (x + size * 23, y), (x + size * 14, y + size * 3.5)])
    list_obj.append(obj)

    brushColor(210, 105, 30)
    mylist = []
    for i in range(91):
        pointX = cos(radians(90 + i)) * size * 3.5
        pointY = sin(radians(90 + i)) * size * 3.5
        pointX, pointY = pointX + x - 9 * size, pointY + y
        mylist.append((pointX, pointY))
    mylist.append((x - 9 * size, y))
    obj = polygon(mylist)
    list_obj.append(obj)

    penColor('black')
    brushColor(255, 228, 181)
    penSize(1)
    obj = polygon([(x + 0.5 * size, y - size * 14), (x + 2 * size, y - size * 7), (x + size * 9, y - size * 7),
                   (x + 0.5 * size, y - size * 14)])
    list_obj.append(obj)
    obj = polygon(
        [(x + 0.5 * size, y), (x + 2 * size, y - size * 7), (x + size * 9, y - size * 7), (x + 0.5 * size, y)])
    list_obj.append(obj)

    brushColor('black')
    penColor('black')
    penSize(0.1)
    obj = circle(x + size * 16, y + size * 1.4, size)
    list_obj.append(obj)
    brushColor('white')
    penColor('white')
    obj = circle(x + size * 16, y + size * 1.4, size * 0.6)
    list_obj.append(obj)
    return list_obj


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


def update():
    global timeTick
    timeTick += 1
    x = 1
    y = 2 * sin(radians(timeTick * 10))
    for i in list_obj:
        moveObjectBy(i, x, y)


def update2():
    global timeTick2
    timeTick2 += 1
    x = 0
    y = 2 * sin(radians(timeTick2 * 10))
    for i in list_obj2:
        moveObjectBy(i, x, y)


def update3():
    global timeTick2
    timeTick2 += 1
    x = 1 * cos(radians(timeTick2 * 5))
    y = 1 * sin(radians(timeTick2 * 5))
    for i in list_obj3:
        moveObjectBy(i, x, y)


canvasSize(1600, 900)
windowSize(1600, 900)
timeTick = 0
timeTick2 = 0
sky()
sea()
beach()
waves()
umbrella(250, 470, 12)
umbrella(800, 580, 10)
list_obj = boat(100, 380, 8) + boat(500, 450, 11)
list_obj2 = cloud(45, 65, 55) + cloud(25, 700, 65) + cloud(45, 1000, 130)
list_obj3 = sun(1400, 150, 80)
onTimer(update, 50)
onTimer(update2, 50)
onTimer(update3, 50)
run()
