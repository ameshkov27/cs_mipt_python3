from random import randint, choice
import tkinter as tk
import math
import time


def main():
    global root, canvas, points, score_widget
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    points = 0
    score_widget = canvas.create_text(30, 30, text=points, font='28')


class Gun:
    def __init__(self, x=20, y=450):
        self.gun_power = 10
        self.gun_status = 0
        self.angle = 1
        self.x = x
        self.y = y
        self.id = canvas.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)

    def charging(self, event):
        self.gun_status = 1

    def discharging(self, event):
        global shells, bullets
        bullets += 1
        start_shell_coord_x = self.x + max(self.gun_power, self.x) * math.cos(self.angle)
        start_shell_coord_y = self.y + max(self.gun_power, self.x) * math.sin(self.angle)
        self.angle = math.atan((event.y - self.y) / (event.x - self.x))
        vx = self.gun_power * math.cos(self.angle)
        vy = -self.gun_power * math.sin(self.angle)
        new_shell = Shell(start_shell_coord_x, start_shell_coord_y, vx, vy)
        shells += [new_shell]
        self.gun_status = 0
        self.gun_power = 10

    def aiming(self, event=0):
        if event:
            self.angle = math.atan((event.y - self.y) / (event.x - self.x))
        if self.gun_status:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, self.x, self.y, self.x + max(self.gun_power, self.x) * math.cos(self.angle),
                      self.y + max(self.gun_power, self.x) * math.sin(self.angle))

    def power_up(self):
        if self.gun_status:
            if self.gun_power < 100:
                self.gun_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Shell:
    def __init__(self, x, y, vx, vy):
        colors = ['red', 'orange', 'black', 'green', 'yellow', 'blue']
        self.r = 10
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                     fill=choice(colors))
        self.live = 30

    def set_coord(self):
        canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        if self.y <= 500:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.set_coord()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 499
            if self.live < 0:
                shells.pop(shells.index(self))
                canvas.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = -self.vx / 2
            self.x = 779


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        x = self.x = randint(600, 780)
        y = self.y = randint(100, 490)
        r = self.r = randint(10, 50)
        self.dx = randint(-10, 10)
        self.dy = randint(-10, 10)
        color = self.color = 'red'
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self):
        canvas.delete(self.id)

    def move(self):
        if self.x >= 770 or self.x <= 500:
            self.dx = -self.dx
        if self.y <= 50 or self.y >= 500:
            self.dy = -self.dy
        self.x += self.dx
        self.y -= self.dy
        canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)


def game_update():
    global root, canvas, shells, gun, targets, bullets_text_widget, bullets, score_widget, points

    shells = []

    gun = Gun()
    targets = [Target() for i in range(2)]
    bullets_text_widget = canvas.create_text(400, 300, text='', font='28')
    bullets = 0

    canvas.bind('<Button-1>', gun.charging)
    canvas.bind('<ButtonRelease-1>', gun.discharging)
    canvas.bind('<Motion>', gun.aiming)

    live = len(targets)
    while live > 0:
        for target in targets:
            target.move()
        for shell in shells:
            shell.move()
            for i, target in enumerate(targets):
                if ((target.x - shell.x) ** 2 + (target.y - shell.y) ** 2) ** 0.5 <= target.r + shell.r:
                    points += 1
                    target.hit()
                    canvas.delete(shell.id)
                    targets.pop(i)
                    live = len(targets)
                    canvas.itemconfig(score_widget, text=points)
            if len(targets) == 0:
                canvas.bind('<Button-1>', '')
                canvas.bind('<ButtonRelease-1>', '')
                canvas.itemconfig(bullets_text_widget, text='Вы уничтожили цели за ' + str(bullets) + ' выстрелов')
        canvas.update()
        time.sleep(0.03)
        gun.aiming()
        gun.power_up()
    for shell in shells:
        canvas.delete(shell.id)
    time.sleep(4)
    canvas.itemconfig(bullets_text_widget, text='')
    canvas.delete(gun.id)
    root.after(1, game_update)


main()
game_update()
root.mainloop()
