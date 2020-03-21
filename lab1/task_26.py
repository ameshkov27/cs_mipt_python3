#!/usr/bin/python3

from pyrob.api import *


def helper():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_left()
    fill_cell()
    move_right(2)
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_left()
    move_up(2)


@task(delay=0.02)
def task_2_4():
    helper()
    for i in range(9):
        move_right(4)
        helper()
    move_down(4)
    helper()
    for i in range(9):
        move_left(4)
        helper()
    move_down(4)
    helper()
    for i in range(9):
        move_right(4)
        helper()
    move_down(4)
    helper()
    for i in range(9):
        move_left(4)
        helper()
    move_down(4)
    helper()
    for i in range(9):
        move_right(4)
        helper()
    while not wall_is_on_the_left():
        move_left()

if __name__ == '__main__':
    run_tasks()
