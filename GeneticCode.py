#!/usr/bin/env python

import sys
from read_file import read_file, parse_codon_table

code = parse_codon_table('codon_table.txt')
rna = read_file(sys.argv[1])

acids = []
for i in range(len(rna)):
    if i%3 == 0:
        acid = code[rna[i:i+3]]
        if acid == 'Stop':
            break
        acids.append(acid)

print(''.join(acids))
