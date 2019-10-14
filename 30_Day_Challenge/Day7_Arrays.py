#!/bin/python3

import math
import os
import random
import re
import sys

def solution(n,arr):
    reverse_arr=[]
    for i in range(n-1,-1,-1):
        reverse_arr.append(arr[i])
    output = ""
    for i in range (len(reverse_arr)):
        output += str(reverse_arr[i]) + ' '

    return output

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(solution(n,arr))
