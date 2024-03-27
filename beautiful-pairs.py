#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    n = len(A)
    a = sorted(A)
    b = sorted(B)
    
    print(a)
    print(b)
    
    pairs = []
    
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                pairs.append([i, j])
                b[j] = 0
                break
            
    add = 1 if len(pairs) != n else 0
            
    print(pairs, len(pairs) + add)
    
    

if __name__ == '__main__':
    n = 6

    A = [1]
    B = [1]

    result = beautifulPairs(A, B)

    print(result)
