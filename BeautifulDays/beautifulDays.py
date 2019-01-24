#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    counter = 0
    for l in range(i,j+1):
        val = abs((l - complementaryDay(l)))/k
        print(val)
        if (val % 1) == 0:
            counter+=1
    return counter

def complementaryDay(i):
    return int(str(i)[::-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
