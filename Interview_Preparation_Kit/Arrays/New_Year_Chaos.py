#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    for i in range (0,len(q)):
        if q [i] > i+3:               #can at most bribe 2 different ppl, means at most moving forward twice.
            print("Too chaotic")
            return            
        else:
            for j in range(max(0,q[i]-2),i):      #to reduce runtime, only choose to begin the loop(for j) from the max position where a larger number may appaears 
                if q[j] > q[i]:
                    count += 1
    print (count)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
