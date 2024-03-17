#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    list = []
    
    """ if n == 1:
        for i in range(0, n + 1):
            list.append(((n - i) * a) + (i * b))
            
        return sorted(list) """
    
    for i in range(0, n):
        res = (((n - 1 - i) * a) + (i * b))
        
        if res not in list:
            list.append(res)
        
    return sorted(list)

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        print(result)
