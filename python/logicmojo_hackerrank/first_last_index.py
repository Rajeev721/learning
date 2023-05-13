#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'search_element' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#

def search_element(arr, target):
    if target not in arr:
        return [-1, -1]

    return [arr.index(target), len(arr) - arr[::-1].index(target) - 1]


if __name__ == '__main__':
    target = 4
    arr = [1,2,3,4,4,4,4,4,4,4,5]
    result = search_element(arr, target)
    print(result)

