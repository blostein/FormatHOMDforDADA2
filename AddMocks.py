#!/usr/bin/env python
import sys
import getopt
import argparse
import glob
import fnmatch
import os
print(__name__)

def main():
    
    taxafile = sys.argv[1]
    ToGenus= sys.argv[2]
    ToSpecies=sys.argv[3]
    ToTaxa_Species = sys.argv[4]
    PathToMockFasta = sys.argv[5]
    
    #change directory to the directory with fasta files
    cwd = os.getcwd()
    MockFolder = cwd+PathToMockFasta
    
    #Create copy of assign taxa to genus file for ammending mocks to end
    # empty list to store contents from reading file
    file_contents = []
    # open file you wish to read
    with open(ToGenus, 'r') as file:
        for line in file:
            file_contents.append(line)
    with open('HOMD_assigntaxa_togenus_plusmocks.fasta', 'w') as newfile:
        for element in file_contents:
            newfile.write(element)
    ToGenusNew='HOMD_assigntaxa_togenus_plusmocks.fasta'
     
    #Add mocks to assign taxa to genus file copy 
    with open(taxafile) as file1, open(ToGenusNew, "a+") as genusfile: 
        for line in file1:
            genus = line.split(';')[5]
            genus_file=genus.strip()+'*.fasta'
        #print(genus_file)
            for file in os.listdir(MockFolder):
                if fnmatch.fnmatch(file, genus_file):
                    with open(os.path.join(MockFolder,file)) as fastafile:
                        count=0
                        for line2 in fastafile: 
                            count+=1
                            if count % 2 == 0:
                                genusfile.write(line)
                                genusfile.write(line2)
                            
    #Create copy of specific species assignment file for dada2 
    #empty list to store contents from reading file
    file_contents = []
    # open file you wish to read
    with open(ToSpecies, 'r') as file:
        for line in file:
            file_contents.append(line)
    with open('HOMD_AssignSpecies_plusmocks.fasta', 'w') as newfile:
        for element in file_contents:
            newfile.write(element)
    ToSpeciesNew='HOMD_AssignSpecies_plusmocks.fasta'
    
    #Add mocks to specific species file 
    with open(taxafile) as file1, open(ToSpeciesNew, "a+") as speciesfile:
        for line in file1:
            genus = line.split(';')[5]
            genus_file=genus.strip()+'*.fasta'
       # print(genus_file)
            for file in os.listdir(MockFolder):
                if fnmatch.fnmatch(file, genus_file):
                    genusname = file.split('_')[0]
                    speciesname = file.split('_')[1]
                    with open(os.path.join(MockFolder,file)) as fastafile:
                        count=0
                        for line2 in fastafile: 
                            count+=1
                            if count % 2 == 0:
                                speciesfile.write('>'+genusname[0]+speciesname[0]+str(count)+' '+genusname+' '+speciesname+'\n')
                                speciesfile.write(line2)
                            
    #create empty file with assign taxa to species file
    file_contents = []
    # open file you wish to read
    with open(ToTaxa_Species, 'r') as file:
        for line in file:
            file_contents.append(line)
    with open('HOMD_AssignTaxaToSpecies_plusmocks.fasta', 'w') as newfile:
        for element in file_contents:
            newfile.write(element)
    ToSpeciesNew='HOMD_AssignTaxaToSpecies_plusmocks.fasta'

    #append mocks to assign taxa to species file 
    with open(taxafile) as file1, open(ToSpeciesNew, "a+") as genusfile: 
        for line in file1:
            genus = line.split(';')[5]
            genus_file=genus.strip()+'*.fasta'
        #print(genus_file)
            for file in os.listdir(MockFolder):
                if fnmatch.fnmatch(file, genus_file):
                    genusname = file.split('_')[0]
                    speciesname = file.split('_')[1]
                    with open(os.path.join(MockFolder,file)) as fastafile:
                        count=0
                        for line2 in fastafile: 
                            count+=1
                            if count % 2 == 0:
                            #genusfile.write(line)
                                genusfile.write(line.strip()+';'+speciesname+';'+'\n')
                                genusfile.write(line2)
                            
if __name__ == "__main__":
    # Define the getopt parameters
    if len(sys.argv) != 6:
        print('need five parameters: \n 1) A .txt. file with the taxonomic levels (to genus) of your mocks bacteria, 2) DADA2 formatted database for assignTaxa to genus level, 3) DADA2 formatted database for assignSpecies, 4) DADA2 formatted database for assignTaxa to species level, 5)path to foled containing .fasta files for mocks (each fasta file named in the following format "genusname_speciesname_#_16S.fasta")')
        sys.exit(-1)
    else:
        main()