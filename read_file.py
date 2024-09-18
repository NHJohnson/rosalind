import sys

def read_file(file_path):
    """ Return contents of stripped first line of file as a string """
    with open(file_path, 'r') as f:
        for line in f:
            text = line.rstrip()
            break
    return text

def read_n_lines(file_path, n=1.5):
    """ Return contents of stripped first n lines of file in a list 
        With the default value of n all lines will be returned
    """
    lines = []
    if n < 1:
        return lines
    with open(file_path, 'r') as f:
        for line in f:
            text = line.rstrip()
            lines.append(text)
            if len(lines) == n:
                break
    return lines   

def read_fasta(file_path):
    """ Return fasta contents as {contig name: sequence} dict"""
    content = {}
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('>'):
                contig = line.rstrip()[1:]
                content[contig] = ''
            else:
                content[contig] += line.rstrip()
    return content          

def parse_codon_table(file_path, mode='rna'):
    """ Read in the codon table and return as a dict 
        Codons are read as rna by default, but 
            if mode is 'dna', U -> T
    """
    all_parts = []
    with open(file_path, 'r') as f:
        for line in f:
            all_parts += line.rstrip().split(' ')
    parts = list(filter(bool, all_parts))
    codons = [j for i, j in enumerate(parts) if not i%2]
    if mode == 'dna':
        codons = [i.replace('U', 'T') for i in codons]
    acids = [j for i, j in enumerate(parts) if i%2]
    return dict(zip(codons, acids))
