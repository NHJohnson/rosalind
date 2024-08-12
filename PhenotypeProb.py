#!/usr/bin/env python

import sys
import read_file

k, m, n = read_file.read_file(sys.argv[1]).split(" ")

k = int(k)
m = int(m)
n = int(n)

total = k + m + n
prob_hom_rec = (n / total) * (((n - 1) / (total - 1)) + .5*( m / (total-1))) \
+ .5*(m / total) * ((n / (total-1)) + .5 * ( (m-1) / (total-1) )) 

print(1 - prob_hom_rec)
