#!/usr/bin/ bash

#Download the sequences

wget http://nematodes.org/teaching/bioinformatics/nem.fasta
makeblastdb -in nem.fasta -dbtype prot -out nem
wget -O testsequence.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_015119.1&strand=1&seq_start=1426&seq_stop=2962&rettype=fasta&retmode=text"
blast -db nem /
 -query testsequence.fasta 
 -outfmt 7 > blastoutput2.out




