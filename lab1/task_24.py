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

@task
def task_2_1():
    move_right()
    move_down()
    helper()


if __name__ == '__main__':
    run_tasks()
