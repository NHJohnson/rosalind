#!/usr/bin/env python3


import sys
filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        x = line.rstrip()
        break

comps = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
revcomp = ''.join([comps[i] for i in x])[::-1]
print(revcomp)
