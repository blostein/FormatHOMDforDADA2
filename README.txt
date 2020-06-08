This folder contains two python files that can be run in the following way: 

cd "YOURPATHTOTHISFOLDER"
python CreateTaxFile.py HOMD_16S_rRNA_RefSeq_V15.2.p9.fasta HOMD_16S_rRNA_RefSeq_V15.2.mothur.taxonomy

python AddMocks.py ZymbiomicsD306MockTaxa.txt DADA2FormattedRef/ToGenusAssignTaxa.fasta DADA2FormattedRef/AssignSpecies.fasta DADA2FormattedRef/ToSpeciesAssignTaxa.fasta /FastaFiles

CreateTaxFile.py requires a HOMD fasta file (unaligned) and the associated mothur formatted taxonomy file (http://www.homd.org/?name=seqDownload&file&type=R)

AddMocks.py requires: 
1) a txt file with the taxonomy (to genus level) of the bacterial strains in the mock community in the following format: 
>Bacteria;Proteobacteria;Gammaproteobacteria;Pseudomonadales;Pseudomonadaceae;Pseudomonas

2-4) DADA2 formatted databases outputed from CreateTaxFile.py in the following order: ToGenusAssignTaxa.fasta, AssignSpecies.fasta, ToSpeciesAssignTaxa.fasta, 
5) Path to a folder containing fasta files (one each per species in mock) with sequences 
    - fasta files in this folder must follow naming convention: GenusName_SpeciesName_16S_3323232.fasta
    - fasta files should look like: 
        >Bacillus_subtilis_16S_1
        TTTATCGGAGAGTTTGATCCTGGCTCAGGACGAACGCTGGC......
        >Bacillus_subtilis_16S_2
        TTTATCGGAGAGTTTGATCCTGGCTCAGGACGAACGTA...