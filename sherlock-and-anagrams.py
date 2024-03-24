#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def is_anagram(a, b):
    return sorted(a) == sorted(b)

def sherlockAndAnagrams(s):
    length = len(s)
    count = 0
    
    for i in range(1, length):
        for x in range(length):
            for y in range(x+1, length):
                a, b = s[x:x+i], s[y:y+i]
                if len(a) == len(b) and is_anagram(a, b):
                    count += 1
    
    return count

if __name__ == '__main__':
    s = 'kkkk'
    
    result = sherlockAndAnagrams(s)

    print (str(result) + '\n')

