#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#


def gridSearch(G, g):
    R = len(G[0])
    r = len(g[0])
    diff = R - r
    
    R_flatten = 'x'.join(G)
    query = '.' + '{' + str(diff + 1) + '}'
    r_flatten = str(f'{query}').join(g)
    
    print(R_flatten)
    print(r_flatten)
    
    match = re.search(rf'{r_flatten}', R_flatten)
    # print(R_flatten)
    # print(r_flatten, diff)
    print(match)
    
    if match:
        print('YES')
    else:
        print('NO')
    
    return  '0'

    


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print (result + "\n")

 