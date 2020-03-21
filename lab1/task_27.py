#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    x = 1
    move_right()
    fill_cell()
    while not wall_is_on_the_right():
        for i in range(x):
            if not wall_is_on_the_right():
                move_right()
                if i == x-1 and not wall_is_on_the_right():
                    fill_cell()
        x += 1


if __name__ == '__main__':
    run_tasks()
