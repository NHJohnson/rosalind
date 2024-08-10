#!/usr/bin/env python3

import sys
filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        x = line.rstrip()
        break

bases = ('A', 'C', 'G', 'T')
print(' '.join([str(x.count(b)) for b in bases]))