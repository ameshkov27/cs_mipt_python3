from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
c_list = []


def new_ball():
    global x, y, r, c_list, n
    c_list = []
    for i in range(rnd(1, 10)):
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(30, 50)
        a = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
        c_list.append({'index': a, 'x': x, 'y': y, 'radius': r})


point = 0


def click(event):
    global c_list, point
    for i, circle in enumerate(c_list):
        length = ((event.x - circle['x']) ** 2 + (event.y - circle['y']) ** 2) ** 0.5
        if length <= circle['radius']:
            point += 1
            print(point)
            canv.delete(circle['index'])
            c_list.pop(i)
            if not len(c_list):
                new_ball()


new_ball()
canv.bind('<Button-1>', click)
mainloop()
