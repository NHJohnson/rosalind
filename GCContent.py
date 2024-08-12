#!/usr/bin/env python3

import sys
from read_file import read_fasta

def get_gc(sequence):
    gc_frac = (sequence.count('C') + sequence.count('G')) / len(sequence)
    return gc_frac

seq_dict = read_fasta(sys.argv[1])

gc_dict = {contig: get_gc(seq) for contig, seq in seq_dict.items()}
max_gc = max(gc_dict.values())
for k,v in gc_dict.items():
    if v == max_gc:
        print(k)
        print(v*100)
        break