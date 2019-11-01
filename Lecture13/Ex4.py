#!/usr/bin/python3

import os


dna="ATGCATCATG"
kmersize=2
minfrequency=2


kmersfound=[]
kmerstars=list(range(0,len(dna)))
print(kmerstarts)

for base in kmerstarts:
	if (base+kmersize)<len(dna)+1:
		seqout=dna[base:+ksize]
		kmersfound=kmersfound+[seqout]
       		nrset=list(set(kmersfound))
       returnstuff=[]

for kfreqfind in nrset:
if kmers.found.count(kfreqfind)>minkfreq:
returnstuff.append(kfreqfind.upper()+": "str(kmersfound.count(kfreqfind)))










#def new_find_my_kmers(dna,ksize=2,minkfreq=2): #function with defaults
#	kmersfound=[]
#	kmerstars=list(range(0,len(dna)))
#	print(kmerstarts)
#	for base in kmerstarts:
#		if (base+kmersize)<len(dna)+1:
#		seqout=dna[base:+ksize]
#		kmersfound=kmersfound+[seqout]
#	nrset=list(set(kmersfound))
#	returnstuff=[]
#	for kfreqfind in nrset:
#		if kmers.found.count(kfreqfind)>minkfreq:
#		returnstuff.append(kfreqfind.upper()+": "str(kmersfound.count(kfreqfind)))
#	return returnstuff


