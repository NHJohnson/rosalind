#!/usr/bin/env python3

"""
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5

Given: A positive integer n≤7

Return: The total number of permutations of length n, 
followed by a list of all such permutations (in any order).
"""

import argparse

def build_permut(nlist):

    if len(nlist) == 1:
        return nlist
    else:
        all_poss = []
        for n in nlist:
            lower_permut = build_permut([i for i in nlist if i != n])
            for sub_permut in lower_permut:
                additor = sub_permut if isinstance(sub_permut, list) else [sub_permut]
                all_poss.append([n] + additor)
        return all_poss

parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int)
args = parser.parse_args()

values = list(range(1, args.n+1))
permuts = build_permut(values)
print(len(permuts))
for p in permuts:
    print(' '.join([str(k) for k in p]))

