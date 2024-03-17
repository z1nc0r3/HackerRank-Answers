#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#


def surfaceArea(A):
    inverted = []
    extra = 0
    up_down = 2 * len(A) * len(A[0])

    for i in range(len(A[0])):
        local_list = list(A[j][i] for j in range(len(A)))
        inverted.append(local_list)

    for each in A:
        total = 0
        total += each[0]
        total += each[-1]
        forward_previous = each[0]
        backward_previous = each[-1]

        for i in range(1, len(each)):
            forward_current = each[i]
            backward_current = each[-i - 1]

            if forward_current < forward_previous:
                total -= forward_current
            elif forward_current > forward_previous:
                total += forward_current
            else:
                total += 0

            if backward_current < backward_previous:
                total -= backward_current
            elif backward_current > backward_previous:
                total += backward_current
            else:
                total += 0

            forward_previous = forward_current
            backward_previous = backward_current

        extra += total

    for each in inverted:
        total = 0
        total += each[0]
        total += each[-1]
        forward_previous = each[0]
        backward_previous = each[-1]

        for i in range(1, len(each)):
            forward_current = each[i]
            backward_current = each[-i - 1]

            if forward_current < forward_previous:
                total -= forward_current
            elif forward_current > forward_previous:
                total += forward_current
            else:
                total += 0

            if backward_current < backward_previous:
                total -= backward_current
            elif backward_current > backward_previous:
                total += backward_current
            else:
                total += 0

            forward_previous = forward_current
            backward_previous = backward_current

        extra += total

    return up_down + extra


if __name__ == "__main__":
    H = 1

    W = 10

    # A = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
    A = [[91, 80, 7, 41, 36, 11, 48, 57, 40, 43]]

    result = surfaceArea(A)

    print(str(result) + "\n")
