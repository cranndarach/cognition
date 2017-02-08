#!/usr/bin/env python3

import random as rd


def scanner():
    plank = ""
    stump = [rd.randrange(2) for i in range(100)]
    for i in range(1, len(stump)):
        if stump[i] > stump[i-1]:
            plank += "|"
    # print(plank)
    return plank


def human(machine_output):
    tree_age = len(machine_output)
    print("This tree must have been {} years old.".format(str(tree_age)))


def main():
    plank_to_read = scanner()
    human(plank_to_read)

if __name__ == "__main__":
    main()
