import tkinter as tk
from random import randint, choice





class Ball:
    def __init__(self):
        colors = ['red', 'orange', 'black', 'green', 'yellow', 'blue']
        delta = [-0.05, -0.04, -0.03, -0.03, -0.02, -0.01, +0.01, +0.02, +0.03, +0.04, +0.05]
        self.r = randint(20, 50)
        self.x = randint(self.r, width_of_window - self.r)
        self.y = randint(self.r, height_of_windows - self.r)
        self.ball_id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                        fill=choice(colors), width=0)
        self.dx, self.dy = choice(delta) * lvl, choice(delta) * lvl

    def move(self):
        canv.move(self.ball_id, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > width_of_window or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r > height_of_windows or self.y - self.r <= 0:
            self.dy = -self.dy

    def returner(self):
        return [self.r, self.ball_id]


def tick():
    for ball in balls:
        ball.move()
    root.after(1, tick)


def delete(event):
    global point
    for i, ball in enumerate(balls):
        dist = ((event.x - int(canv.coords(ball.returner()[1])[0] + ball.returner()[0])) ** 2 + (
                event.y - int(canv.coords(ball.returner()[1])[1] + ball.returner()[0])) ** 2) ** 0.5
        if dist <= ball.returner()[0]:
            canv.delete(ball.returner()[1])
            point += 1
            if winscore == point:
                exit('ПОБЕДА')
            balls.pop(i)
            print(point)
        if not len(balls):
            main()


def main():
    global balls

    balls = [Ball() for i in range(randint(1, 10))]

    tick()
    canv.bind('<Button-1>', delete)


if __name__ == "__main__":
    lvl = int(input('Введите уровень игры'))
    point = 0
    winscore = 35
    width_of_window = 800
    height_of_windows = 600
    root = tk.Tk()
    root.geometry('{}x{}'.format(width_of_window, height_of_windows))
    root.wm_attributes('-topmost', 1)
    canv = tk.Canvas(root, bg='white')
    canv.pack(fill=tk.BOTH, expand=1)
    main()
    tk.mainloop()
