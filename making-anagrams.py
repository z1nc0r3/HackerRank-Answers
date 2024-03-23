#!/bin/python3

import math
import os
import random
import re
import sys

def makingAnagrams(s1, s2):
    s1_list = [i for i in s1]
    s2_list = [i for i in s2]
    intersect = []
    
    for char in s1_list:
        if char in s2_list:
            intersect.append(char)
            s2_list.remove(char)
            
    print(intersect)
    
    return len(s1 + s2) - 2 * len(intersect)

if __name__ == '__main__':

    s1 = 'bascsdfse'

    s2 = 'sasdfscswras'

    result = makingAnagrams(s1, s2)

    print(result)
