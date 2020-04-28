#!/usr/bin/env python
import sys
import numpy as np
import getopt
import argparse
import itertools
print(__name__)

def main():
    
    fasta_file = sys.argv[1]
    taxa_file = sys.argv[2]
    
    filenew= open("ToSpeciesAssignTaxa.fasta","w+")
    with open(fasta_file) as file1, open(taxa_file) as file2:
        for line1, line2 in zip(itertools.zip_longest(*[file1]*2), file2):
            if line1[0].split()[0][1:]==line2.split()[0]:
                filenew.write('>'+line2.split()[1]+"\n")
                filenew.write(line1[1])
            
    filenew2= open("AssignSpecies.fasta","w+")
    with open(fasta_file) as file1, open(taxa_file) as file2:
        for line1, line2 in zip(itertools.zip_longest(*[file1]*2), file2):
            if line1[0].split()[0][1:]==line2.split()[0]:
                filenew2.write(line1[0].split()[0]+" "+line2.split()[1].split(";")[5]+" "+line2.split()[1].split(";")[6]+"\n")
                filenew2.write(line1[1])

    filenew3= open("ToGenusAssignTaxa.fasta","w+")
    with open(fasta_file) as file1, open(taxa_file) as file2:
        for line1, line2 in zip(itertools.zip_longest(*[file1]*2), file2):
            if line1[0].split()[0][1:]==line2.split()[0]:
                filenew3.write('>'+";".join(line2.split()[1].split(';')[0:6])+"\n")
                filenew3.write(line1[1])

if __name__ == "__main__":
    # Define the getopt parameters
    if len(sys.argv) != 3:
        print('need two filenames - a fasta and a taxonomy file - did you not give one?')
        sys.exit(-1)
    else:
        main()