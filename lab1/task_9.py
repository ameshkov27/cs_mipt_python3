#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    if wall_is_above() is False and wall_is_beneath():
        fill_cell()
    while wall_is_on_the_right() is False:
        move_right()
        if wall_is_above() is False and wall_is_beneath():
            fill_cell()


if __name__ == '__main__':
    run_tasks()
