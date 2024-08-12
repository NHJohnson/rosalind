#!/usr/bin/env python3

import sys
from read_file import read_n_lines

sequences = read_n_lines(sys.argv[1], 2)

hamdist = sum(i != j for i, j in zip(sequences[0], sequences[1]))

print(hamdist)