#!/bin/python3


import os

#K-mers are short DNA sub-sequences with length "k" bases, and are usually generated using the sliding window method we used in the last lecture's exercise. Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than some number (n) of times (you chose what that number is). 

#Example:
#dna="ATGCATCATG"
#k=2
#n=2

#output shsould be AT because the kmers are 2 bases long,and there are 3 instances at

# We need something generic that we could maybe plug numbers in as and when needed.

# Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than n times.

# INPUT a made-up test sequence, assume it's good and all lower case
#len(sequencein)=97
sequencein = "atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatatc"
sequencein

# Possible_kmer_sizes
bb=list(range(2,int(len(sequencein)-1))) #this goes from 2 to 95

# Arbitrarily choose a smaller set (2-6) for now!
possible_kmer_sizes=list(range(2,7))
possible_kmer_sizes

# Set the minimum frequency
kmerfound_minimum=3 #n

# PROCESS using a for loop for the kmer sizes
for window in possible_kmer_sizes:
	kmersfound=[]
	kmerrange=list(range(0,len(sequencein))) #kmerrange is 0-96
#	kmerrange
# Also use a for loop for getting the kmer sequences
        for startingbase in kmerrange:
                if (startingbase+window)<len(sequencein)+1:
			seqout=(sequencein)[startingbase:startingbase+window]
			seqout
			kmersfound=kmersfound + [seqout]
			kmersfound
# OUTPUT the frequencies of the non-redundant set of kmer sequences
			nonredundantset = list(set(kmersfound))
                        for kmerfrequencies in nonredundantset:
                                if kmersfound.count(kmerfrequencies) > kmerfound_minimum :
                                        print("Lots! " + str(kmerfrequencies)+" "+str(kmersfound.count(kmerfrequencies)))
                                else:
                                        print(str(kmerfrequencies) + " " + str(kmersfound.count(kmerfrequencies)))
