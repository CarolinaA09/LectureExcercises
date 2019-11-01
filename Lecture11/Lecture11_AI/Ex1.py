#!/bin/python

import os

mosca3=open("data.csv")

mosca_read=mosca3.read().rstrip().split("\n")



for everyline in mosca_read:
	lines=everyline.split(",")
	print(lines)
	names=lines[0]
	print(names)
	geneseqs=lines[1].upper()
	seqlenghts=len(lines[1])
	genenames=lines[2]
	expressionlevel=int(lines[3])
	ATcontent=(geneseqs.count('A')+geneseqs.count('T'))/seqlengths
	atstatus="low"
	if (atcontent >= 0.45 and atcontent <= 0.65):
	if 

	
