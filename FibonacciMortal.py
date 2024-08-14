#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m')
parser.add_argument('-n')
args = parser.parse_args()

young_dict = {}
def nyoung(n, m):
    if n in young_dict:
        return young_dict[n]
    elif n < 1:
        answer = 0
    elif n == 1:
        answer = 1
    else:
        answer = ngrown(n-1, m)
    young_dict[n] = answer
    return answer

grown_dict = {}
def ngrown(n, m):
    if n in grown_dict:
        return grown_dict[n]
    elif n < 2:
        answer = 0
    else:
        answer = total(n-1, m) - nyoung(n-m, m)
    grown_dict[n] = answer
    return answer

def total(n, m):
    return nyoung(n,m) + ngrown(n,m)

#in_string = read_file(sys.argv[1])
#n, m = in_string.rstrip().split(' ')
n = int(args.n)
m = int(args.m)

print(total(n, m))

