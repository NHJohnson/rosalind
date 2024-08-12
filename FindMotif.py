#!/usr/bin/env python

import re
import sys
from read_file import read_n_lines

s, t = read_n_lines(sys.argv[1], 2)
regex = re.compile('(?='+t+')')
all_starts = []
for m in regex.finditer(s):
    all_starts.append(str(m.start() + 1))
print(' '.join(all_starts))
