"""
task @group description
.. task @code make a new tasklr
.. create task 1 in group code

task list @group
.. task list @code
.. @code:
..  1. [status] make a new tasklr
"""

from tasklr import cli


def main():
    cli.main()


if __name__ == "__main__":
    main()

