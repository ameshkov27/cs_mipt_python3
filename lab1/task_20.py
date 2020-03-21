#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for i in range(12):
        for j in range(26):
            if i % 2 == 0:
                fill_cell()
                move_right()
                fill_cell()
            else:
                fill_cell()
                move_left()
                fill_cell()
        move_down()

if __name__ == '__main__':
    run_tasks()
