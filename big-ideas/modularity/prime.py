#!/usr/bin/env python3

"""
A Python script for determining whether a number is prime, based on an
example from class. It separates the problem into parts for determining
whether a number is divisible by another, finding a number's greatest
non-self factor, and determining whether the input number is a special
case (i.e., 0, 1, or 2). It could be modularized further, for example
by separating the while loop into its own function, if one wanted.
"""

import time


def evenly_divides(num_a, num_b):
    return True if (num_a % num_b == 0) else False


def biggest_possible_factor(num):
    return int(num/2)


def specifics(num):
    if num in [0, 1]:
        return False
    elif num == 2:
        return True
    else:
        return None


def is_prime(num):
    if specifics(num) != None:
        return specifics(num)
    stop_val = biggest_possible_factor(num)
    candidate = 2
    while candidate <= stop_val:
        if evenly_divides(num, candidate):
            return False
        else:
            candidate += 1
    else:
        return True

if __name__ == "__main__":
    my_num = int(time.time())
    print("Time: {}".format(str(my_num)))
    print(is_prime(my_num))
