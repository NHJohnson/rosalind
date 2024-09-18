#!/usr/bin/env python3

"""
Either strand of a DNA double helix can serve as the coding strand for 
RNA transcription. Hence, a given DNA string implies six total reading 
frames, or ways in which the same region of DNA can be translated into 
amino acids: three reading frames result from reading the string itself,
 whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon 
and ends by stop codon, without any other stop codons in between. 
Thus, a candidate protein string is derived by translating an open 
reading frame into amino acids until a stop codon is reached.

Given: A DNA string s

of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated 
from ORFs of s
. Strings can be returned in any order.
"""

import re
import sys

from read_file import read_fasta, parse_codon_table
from revcomp import revcomp

def get_prot_strings(dna, codon_table):
    """ Return a list of all protein strings that can be generated
            from a dna sequence
        Generally there are 6 such strings, being associated with 
            3 frames on each strand
    """
    all_prot_seq = []
    for seq in (dna, revcomp(dna)):
        for idx in range(3):
            protseq = []
            for pos in range(len(dna) - 2):
                if pos % 3 == idx:
                    protseq.append(codon_table[seq[pos:pos+3]])
            all_prot_seq.append(''.join(protseq))
    return all_prot_seq 

sequences = read_fasta(sys.argv[1])
codon_table = parse_codon_table(sys.argv[2], mode='dna')

dna_seq = list(sequences.values())[0]
all_prot_strings = get_prot_strings(dna_seq, codon_table)

orf = re.compile('(?=(M[A-Z]*(?=Stop)))')
all_orfs = []
for prot_str in all_prot_strings:
    matches = re.finditer(orf, prot_str)
    for match in matches:
        all_orfs.append(match[1])

for orf in set(all_orfs):
    print(orf)



