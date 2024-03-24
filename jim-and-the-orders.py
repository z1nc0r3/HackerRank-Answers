#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    serve_time = [orders[i][0] + orders[i][1] for i in range(len(orders))]

    result = {i + 1: serve_time[i] for i in range(len(serve_time))}

    sorted_res = dict(sorted(result.items(), key=lambda item: item[1]))
    
    return (' '.join(map(str, list(sorted_res.keys()))))

if __name__ == '__main__':

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    print(result)
