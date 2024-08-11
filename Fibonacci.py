#!/usr/bin/env python3

import sys
from read_file import read_file

def fibonacci_value(n, k):
    """ Get the value of the Fibonacci sequence for values n and k """
    if n == 1 or n == 2:
        return 1
    else: 
        return fibonacci_value(n-1, k) + k * fibonacci_value(n-2, k)

in_string = read_file(sys.argv[1])
n, k = in_string.rstrip().split(' ')
n = int(n)
k = int(k)

print(fibonacci_value(n, k))

