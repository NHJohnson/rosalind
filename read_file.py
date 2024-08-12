import sys

def read_file(file_path):
    """ Return contents of stripped first line of file as a string """
    with open(file_path, 'r') as f:
        for line in f:
            text = line.rstrip()
            break
    return text

def read_n_lines(file_path, n):
    """ Return contents of stripped first n lines of file in a list """
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

def parse_codon_table(file_path):
    """ Read in the codon table and return as a dict """
    all_parts = []
    with open(file_path, 'r') as f:
        for line in f:
            all_parts += line.rstrip().split(' ')
    parts = list(filter(bool, all_parts))
    codons = [j for i, j in enumerate(parts) if not i%2]
    acids = [j for i, j in enumerate(parts) if i%2]
    return dict(zip(codons, acids))
