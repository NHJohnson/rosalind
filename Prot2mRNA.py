#!/usr/bin/env python3

import sys

from read_file import read_file, parse_codon_table

codon_dict = parse_codon_table('codon_table.txt')
prot_list = list(codon_dict.values())
codon_redundancy = {prot: prot_list.count(prot) for prot in set(prot_list)}

prot_string = read_file(sys.argv[1])
# 3 possible stop codons
prot_string_redund = [codon_redundancy[aa] for aa in prot_string] + [3]

poss = 1
for p in prot_string_redund:
    poss *= p
    poss = poss % 1000000

print(poss)

