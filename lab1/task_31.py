#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while not wall_is_beneath():
        move_down()
    while True:
        x = 1
        y = 1
        while not wall_is_on_the_left():
            move_left()
            x += 1
        while not wall_is_on_the_right() and wall_is_beneath():
            move_right()
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
                y = 1
            y += 1
        if y == x:
            while not wall_is_on_the_left():
                move_left()
            break


if __name__ == '__main__':
    run_tasks()
