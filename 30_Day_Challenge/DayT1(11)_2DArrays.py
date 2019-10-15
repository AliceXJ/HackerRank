#!/bin/python3

import math
import os
import random
import re
import sys

def solution(arr):
    h_sum=0
    max_sum = arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2]
    for i in range(1,5):
        for j in range(1,5):
            h_sum = arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            if h_sum > max_sum:
                max_sum = h_sum
    return max_sum
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print (solution(arr))
