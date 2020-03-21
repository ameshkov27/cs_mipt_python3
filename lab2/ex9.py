import turtle
import math

turtle.shape('turtle')


def polygon(n, a):
    for i in range(n):
        turtle.forward(a)
        turtle.left(360 / n)


turtle.speed(1)
turtle.left(35)
R = 15
z = 125
for n in range(3, 12):
    a = R * 2 * math.sin(2 * math.pi / (2 * n))
    polygon(n, a)
    turtle.right(z)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.left(z)
    z -= 5
    R += 15
