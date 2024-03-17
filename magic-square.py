#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(s):
    # Write your code here
    mv = [2, 7, 6, 1, 8, 3, 4, 9]
    rev_mv = [8, 1, 6, 7, 2, 9, 4, 3]
    min_diff = 45

    middle_diff = abs(s[1][1] - 5)

    around = [
        s[0][0],
        s[0][1],
        s[0][2],
        s[1][2],
        s[2][2],
        s[2][1],
        s[2][0],
        s[1][0]
    ]

    around = deque(around)

    for j in range(4):
        around.rotate(2)
        diff = sum([abs(mv[i] - around[i]) for i in range(8)])
        rev_diff = sum([abs(rev_mv[i] - around[i]) for i in range(8)])

        if min(diff, rev_diff) < min_diff:
            min_diff = min(diff, rev_diff)

    min_diff += middle_diff

    return min_diff


if __name__ == "__main__":

    s = [[6, 1, 2], [7, 2, 6], [5, 6, 2]]

    result = formingMagicSquare(s)

    print(str(result) + "\n")
