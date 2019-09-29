#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    already_checked = []
    sum_pair = 0
    for i in range (0,n):
        if ar[i] not in already_checked:
            count = 0
            for j in range (0,n):
                if ar[j] == ar[i]:
                    count = count + 1
            already_checked.append(ar[i])
            sum_pair += int(count/2)
    return sum_pair
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
