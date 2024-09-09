#!/usr/bin/env python3
""" Identify the longest common substring of a group of strings """

import sys
from read_file import read_fasta

def get_all_substrings(string):
    """ 
    Given a string, return a dictionary whose keys are
    all the substrings of the string, and whose values
    are all the lengths of those substrings
    """
    subseq = {string: len(string)}
    for strlen in range(1, len(string)):
        for pos in range(0, len(string)-strlen+1):
            seq = string[pos:pos+strlen]
            if seq not in subseq:
                subseq[seq] = len(seq)
    return subseq

sequences = list(read_fasta(sys.argv[1]).values())
subseq = get_all_substrings(sequences[0])
for seq in sequences[1:]:
    for key in list(subseq):
        if key not in seq:
            subseq.pop(key)
longest = max(subseq.keys(), key=lambda x: subseq[x])
print(longest)
