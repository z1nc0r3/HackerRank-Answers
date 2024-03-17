#!/bin/python3

import math
import os
import random
import re
import sys


def intersection(a, b):
    list = [value for value in a if value in b]
    return len(list) == 0


def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])
    max_index = []
    max_areas = []
    max_area = 0

    for i in range(n):
        for j in range(m):
            sub_list = []

            if grid[i][j] == "B":
                continue
            else:
                sub_list.append([i, j])

            for shift in range(1, min(n, m)):
                try:
                    if (
                        i - shift < 0
                        or j - shift < 0
                        or i + shift > n - 1
                        or j + shift > m - 1
                    ):
                        raise Exception

                    top = grid[i - shift][j]
                    bottom = grid[i + shift][j]
                    left = grid[i][j - shift]
                    right = grid[i][j + shift]

                    if top == "G" and bottom == "G" and left == "G" and right == "G":
                        sub_list.append([i - shift, j])
                        sub_list.append([i + shift, j])
                        sub_list.append([i, j - shift])
                        sub_list.append([i, j + shift])
                        max_index.append(sub_list.copy())
                    else:
                        raise Exception
                except:
                    max_index.append(sub_list)
                    break

    max_index = sorted(max_index, key=lambda x: len(x), reverse=True)

    length = len(max_index)

    if len(max_index) == 2:
        return len(max_index[0]) * len(max_index[1])

    for i in range(length - 2):
        for j in range(i + 1, length):
            if intersection(max_index[i], max_index[j]):
                max_area = len(max_index[i]) * len(max_index[j])
                max_areas.append(max_area)

    if len(max_areas) == 0:
        return 0

    return max(max_areas)


if __name__ == "__main__":

    n = 12
    m = 12

    grid = [
        "GGGGGGGGGGGG",
        "GBGGBBBBBBBG",
        "GBGGBBBBBBBG",
        "GGGGGGGGGGGG",
        "GGGGGGGGGGGG",
        "GGGGGGGGGGGG",
        "GGGGGGGGGGGG",
        "GBGGBBBBBBBG",
        "GBGGBBBBBBBG",
        "GBGGBBBBBBBG",
        "GGGGGGGGGGGG",
        "GBGGBBBBBBBG",
    ]

    result = twoPluses(grid)

    print(str(result) + "\n")
