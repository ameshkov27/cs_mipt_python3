import turtle

turtle.shape('turtle')


def circle(flag):
    if flag == 'l':
        for i in range(360):
            turtle.forward(1)
            turtle.left(1)
    else:
        for i in range(360):
            turtle.forward(1)
            turtle.right(1)


for i in range(3):
    circle('l')
    circle('r')
    turtle.left(60)

input()
