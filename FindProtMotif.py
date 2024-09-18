#!/usr/bin/env python

import re
import sys
import urllib.request

from read_file import read_n_lines, read_fasta

protein_ids = read_n_lines(sys.argv[1])

nglyc = re.compile('(?=(N[^P][ST][^P]))')

for p in protein_ids:
    prot_id = p.split('_')[0]
    url = 'https://rest.uniprot.org/uniprotkb/%s.fasta' % prot_id
    urllib.request.urlretrieve(url, '%s.fasta' % prot_id)
    seq_dict = read_fasta('%s.fasta' % prot_id)
    for seqname, sequence in seq_dict.items():
        matches = re.finditer(nglyc, sequence)
        starts = [i.start() + 1 for i in matches]
        if starts:
            print(p)
            print(' '.join([str(j) for j in starts]))



