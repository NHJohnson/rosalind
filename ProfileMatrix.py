#!/usr/bin/env python3

import numpy as np
import sys
from read_file import read_fasta

bases = ('A', 'C', 'G', 'T')

sequences = read_fasta(sys.argv[1]).values()
seq_array = np.array([list(i) for i in sequences])
print(''.join([max(bases, key=lambda x: np.count_nonzero(column == x)) for column in seq_array.T]))
for base in bases:
    print(base+':', ' '.join([str(i) for i in np.count_nonzero(seq_array == base, axis=0)]))
