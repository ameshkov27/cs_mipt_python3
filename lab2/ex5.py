import turtle

turtle.shape('turtle')


def square(x):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)


x = 30

for i in range(10):
    square(x)
    turtle.right(45)
    turtle.penup()
    turtle.forward(13.5)
    turtle.pendown()
    turtle.left(135)
    x += 20
