import turtle

turtle.shape('turtle')


def circle(flag, n):
    if flag == 'l':
        for i in range(360):
            turtle.forward(n)
            turtle.left(1)
    else:
        for i in range(360):
            turtle.forward(n)
            turtle.right(1)


turtle.left(90)
n = 0.5
for i in range(10):
    circle('l', n)
    circle('r', n)
    n += 0.1
