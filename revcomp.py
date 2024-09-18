#!/usr/bin/env python3


def revcomp(sequence):
    """ return the reverse complement of sequence """
    comps = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    revcomp = ''.join([comps[i] for i in sequence])[::-1]
    return revcomp
