import turtle

turtle.shape('turtle')


def half_circle(flag):
    if flag == 'b':
        for i in range(180):
            turtle.forward(0.5)
            turtle.right(1)
    else:
        for i in range(180):
            turtle.forward(0.1)
            turtle.right(1)


turtle.left(90)
for i in range(5):
    half_circle('b')
    if i != 4:
        half_circle('l')
