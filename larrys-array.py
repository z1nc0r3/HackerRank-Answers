#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#


def larrysArray(A):
    length = len(A)

    for round in range(length):
        print(round)
        og = A.copy()
        for i in range(length - 2):

            sub_list = [A[i + j] for j in range(3)]
            while min(sub_list) != sub_list[0]:
                sub_list = deque(sub_list)
                sub_list.rotate(-1)
                sub_list = list(sub_list)
                print(sub_list, A)

            for j in range(3):
                A[i + j] = sub_list[j]
            print(A)
            print()

        if A == og:
            break

    if A[-2] > A[-1]:
        return "NO"

    return "YES"


if __name__ == "__main__":
    n = 12

    # A = [1, 6, 5, 2, 4, 3]
    A = [21, 89, 91, 43, 103, 13, 36, 2, 101, 7, 16, 113, 20, 17, 39, 14, 46, 15, 105, 85, 3, 74, 62, 99, 51, 33, 65, 55, 22, 47, 79, 59, 19, 29, 66, 50, 35, 61, 112, 68, 37, 84, 57, 73, 70, 107, 53, 42, 6, 49, 102, 45, 93, 98, 18, 88, 58, 64, 31, 9, 97, 90, 78, 32, 80, 83, 108, 34, 56, 76, 110, 86, 24, 77, 28, 96, 8, 72, 82, 109, 5, 100, 38, 87, 71, 94, 60, 27, 75, 1, 52, 92, 23, 12, 4, 30, 40, 10, 95, 67, 111, 44, 81, 104, 69, 11, 54, 26, 41, 106, 63, 48, 25]

    result = larrysArray(A)

    print(result + "\n")
