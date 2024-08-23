#!/usr/bin/env python3

import sys
from OverlapGraph import OverlapGraph

fasta = sys.argv[1]
k = int(sys.argv[2])

graph = OverlapGraph.from_fasta(fasta)
graph.print_adjacency_list(k)
