#!/usr/bin/env python3

import sys
filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        seq = line.rstrip()
        break

print(seq.replace('T', 'U'))
