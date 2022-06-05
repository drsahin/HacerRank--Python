# Objective
# Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.

# Example
# n=125
# The binary representation of (125)10 is (1111101)2. In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.

# Input Format

# A single integer, n.

# Constraints
# 1<=n<=10**6
# Output Format

# Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

# Sample Input 1

# 5
# Sample Output 1

# 1
# Sample Input 2

# 13
# Sample Output 2

# 2


# SOLUTİON:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    numbers = str(bin(n)[2:]).split('0')
    lenghts = [len(num) for num in numbers]
    print(max(lenghts))


# SOLUTİON:2
N = int(input())
DATA = bin(N)

MAXIMUM = 0
CURRENT = 0

for num in DATA:
    if num == '1':
        CURRENT = CURRENT + 1
    else:
        MAXIMUM = max(MAXIMUM, CURRENT)
        CURRENT = 0

print(max(MAXIMUM, CURRENT))