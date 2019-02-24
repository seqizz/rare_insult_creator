#!/usr/bin/env python3
import random


def find_one_random(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()
        random_int = random.randint(0, len(lines)-1)
        return lines[random_int].rstrip()

print('{} {} {}'.format(
    find_one_random('adjective'),
    find_one_random('curse'),
    find_one_random('noun')
))
