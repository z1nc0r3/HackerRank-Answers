#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    new_char = []
    new_str = []
    upper = [i for i in range(len(s)) if s[i].isupper()]
    s = s.lower()

    for char in s:
        if char.islower():
            new_char.append((ord(char) + k - 97) % 26 + 97)
        else:
            new_char.append(ord(char))

    for ascii in new_char:
        new_str.append(chr(ascii))

    for pos in upper:
        new_str[pos] = new_str[pos].upper()

    print("".join(new_str))


if __name__ == "__main__":
    n = 10

    s = "Middle-Outz"

    k = 2

    result = caesarCipher(s, k)

    print(result)
