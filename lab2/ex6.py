import turtle

turtle.shape('turtle')


def spider(n):
    for i in range(n):
        turtle.right(360 / n)
        turtle.forward(90)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(90)
        turtle.right(180)


spider(12)
