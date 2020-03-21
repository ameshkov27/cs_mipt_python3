import turtle

turtle.shape('turtle')


def half_circle():
    for i in range(180):
        turtle.forward(0.3)
        turtle.left(1)


def circle(n):
    for i in range(360):
        turtle.forward(n)
        turtle.left(1)


turtle.fillcolor('yellow')
turtle.begin_fill()
circle(1)
turtle.end_fill()

turtle.penup()
turtle.goto(-20, 80)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
circle(0.1)
turtle.end_fill()

turtle.penup()
turtle.goto(20, 80)
turtle.pendown()

turtle.begin_fill()
circle(0.1)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 60)
turtle.pendown()

turtle.width(3)
turtle.goto(0, 50)

turtle.penup()
turtle.goto(-17, 30)
turtle.pendown()

turtle.color('red')
turtle.left(270)
half_circle()
