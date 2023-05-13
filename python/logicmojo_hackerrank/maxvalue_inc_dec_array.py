#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findmax_value' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findmax_value(arr):
    low_value = 0
    high_value = len(arr)-1
    while(low_value <= high_value):
        mid_value = (low_value+high_value)//2
        # This is for array of 1,2 or 3 elements
        if high_value == mid_value:
            return arr[mid_value]
        if arr[mid_value] > arr[mid_value - 1] and arr[mid_value] > arr[mid_value + 1]:
            return arr[mid_value]
        if arr[mid_value] < arr[mid_value + 1] and arr[mid_value] > arr[mid_value - 1]:
            low_value = mid_value + 1
        else:
            high_value = mid_value - 1
if __name__ == '__main__':
    result = findmax_value([1,2,3,6,7,45,56,67,78,9,7,6,4,3,2])
    print(result)
