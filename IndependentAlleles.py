#!/usr/bin/env python3

"""
Given: Two positive integers k (k≤7) and N (N≤2^k). 
In this problem, we begin with Tom, who in the 0th generation has 
genotype Aa Bb. Tom has two children in the 1st generation, 
each of whom has two children, and so on. Each organism always 
mates with an organism having genotype Aa Bb.

Return: The probability that at least N
Aa Bb organisms will belong to the k-th generation of Tom's 
family tree (don't count the Aa Bb mates at each level). Assume that 
Mendel's second law holds for the factors.
"""

import argparse
import random
from scipy.stats import binom

class Individual():

    def __init__(self, genotype):
        if len(genotype) != 2:
            raise ValueError('Genotype must have 2 traits')
        if len(genotype[0]) != 2:
            raise ValueError('Trait 1 must have 2 alleles')
        if len(genotype[1]) != 2:
            raise ValueError('Trait 2 must have 2 alleles')
        for allele in genotype[0]:
            if allele not in ['a', 'A']:
                raise ValueError('All alleles for trait 1 must be a or A')
        for allele in genotype[1]:
            if allele not in ['b', 'B']:
                raise ValueError('All alleles for trait 1 must be b or B')
            
        self.genotype = genotype

    @staticmethod
    def cross_gt(gt1, gt2):
        """ Produce a new genotype by crossing the inputs """
        trait1 = sorted([random.choice(gt1[0]), random.choice(gt2[0])])
        trait2 = sorted([random.choice(gt1[1]), random.choice(gt2[1])])
        return [trait1, trait2]

    @classmethod
    def fromParent(cls, parent):
        other_parent_gt = [['A', 'a'], ['B', 'b']]
        new_gt = cls.cross_gt(parent.genotype, other_parent_gt)
        return cls(new_gt)
    
parser = argparse.ArgumentParser()
parser.add_argument('-k', type=int)
parser.add_argument('-N', type=int)
args = parser.parse_args()

"""
tom = Individual([['A', 'a'], ['B', 'b']])
current_gen = [tom]

for idx in range(args.k):
    new_gen = []
    for person in current_gen:
        for jdx in range(2):
            new_gen.append(Individual.fromParent(person))
    current_gen = new_gen

print(len([1 for i in current_gen if i.genotype == [['A', 'a'], ['B', 'b']]]))
"""

print(binom.sf(args.N-1, 2**args.k, 0.25))