#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_on_the_left() is False:
        move_left()
    elif wall_is_above() is False:
        move_up()
    elif wall_is_on_the_right() is False:
        move_right()
    else:
        move_down()


if __name__ == '__main__':
    run_tasks()
