#!/usr/bin/python3

from pyrob.api import *


def helper(n):
    if n-2 >= 1:
        for i in range(n - 2):
            move_left()
            fill_cell()
        move_left()
        for i in range(n - 2):
            move_down()
            fill_cell()
        move_down()
        for i in range(n - 2):
            move_right()
            fill_cell()
        move_right()
        for i in range(n -2 ):
            move_up()
            fill_cell()
        move_left()

@task(delay=0.5)
def task_9_3():
    x = 1
    while not wall_is_on_the_right():
        move_right()
        x += 1
    while x > 1:
        helper(x)
        x -= 2
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()
if __name__ == '__main__':
    run_tasks()
