#!/usr/bin/env python3

"""
Given: Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population 
possessing each genotype pairing for a given factor. 
In order, the six given integers represent the number of couples
having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant 
phenotype in the next generation, under the assumption that every 
couple has exactly two offspring.
"""

import numpy as np
import sys
from read_file import read_file

numbers_string = read_file(sys.argv[1])
ncouples = np.array([int(i) for i in numbers_string.split(" ")])

prob_dominant = np.array([1, 1, 1, 0.75, 0.5, 0])

offspring_by_genotype = ncouples * prob_dominant

print(2*np.sum(offspring_by_genotype))
