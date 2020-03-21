import turtle

turtle.shape('turtle')

x = 0.05

for i in range(360):
    turtle.forward(x)
    turtle.left(5)
    x += 0.01
