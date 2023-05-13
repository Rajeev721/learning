#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'find_missing' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def find_missing(arr):
    # Write your code here

    length = len(arr)
    num = length - (((length * (length + 1)) / 2) - sum(arr))
    for i in range(length):
        if arr.count(i) == 2:
            return str(list([arr[i], num]))


if __name__ == '__main__':
    arr = [1,2,3,4,4,5,5,6]
    result = find_missing(arr)
    print(result)
