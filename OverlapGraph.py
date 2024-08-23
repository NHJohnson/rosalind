""" Class for an overlap graph """

from collections import defaultdict

from read_file import read_fasta

class OverlapGraph():

    def __init__(self, kmers = {}):
        self.kmers = kmers
        self.suffixes = {}
        self.prefixes = {}
        self.adjacency_built = False
    
    @classmethod
    def from_fasta(cls, fasta):
        """ Parse a fasta and initialize from sequences found there"""
        sequences = read_fasta(fasta)
        return cls(kmers = sequences)

    def build_suffixes(self, k):
        """ Create dictionary of all suffixes of length k in self.kmers
                with values being a list of kmers to which they belong
        """
        suffixes = defaultdict(list)
        for label, kmer in self.kmers.items():
            suffix = kmer[-k:]
            suffixes[suffix].append(label)
        self.suffixes[k] = suffixes

    def build_prefixes(self, k):
        """ Create dictionary of all prefixes of length k in self.kmers
                with values being a list of kmers to which they belong
        """
        prefixes = defaultdict(list)
        for label, kmer in self.kmers.items():
            prefix = kmer[:k]
            prefixes[prefix].append(label)
        self.prefixes[k] = prefixes

    def build_adjacency_list(self, k):
        """ Create adjacency list of kmers for O(k) """
        self.adjacency_list = []
        self.build_prefixes(k)
        self.build_suffixes(k)
        for suffix, suf_labels in self.suffixes[k].items():
            for label_i in suf_labels:
                for label_j in self.prefixes[k][suffix]:
                    if label_i != label_j:
                        self.adjacency_list.append((label_i, label_j))
        self.adjacency_built = True

    def print_adjacency_list(self, k):
        """ Print the adjacency list O(k) """
        if not self.adjacency_built:
            self.build_adjacency_list(k)
        for pair in self.adjacency_list:
            print(' '.join(pair))

