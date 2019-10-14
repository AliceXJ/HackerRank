#!/bin/python3

import math
import os
import random
import re
import sys

def solution(n):
    count = 0
    max_c = 0
    while(n > 0):
        if n%2 ==0:
            count = 0
        else:
            count +=1
            if max_c < count:
                max_c = count
        n = n//2
    return max_c
if __name__ == '__main__':
    n = int(input())
    print(solution(n))
