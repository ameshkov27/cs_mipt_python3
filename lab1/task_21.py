#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    n = 13
    while n > 0:
        if n % 2 != 0 :
            for i in range(n):
                move_right()
                move_down()
                fill_cell()
            move_down()
        else:
            for i in range(n):
                move_left()
                move_up()
                fill_cell()
            move_left()
        n -= 1



if __name__ == '__main__':
    run_tasks()
