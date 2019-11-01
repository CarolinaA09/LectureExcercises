#!/bin/python

#Here is a list of DNA sequences that are all equal in length, with varying degrees of similarity:

input_seqs=['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT'] 

#Write a programme/script that calculates and prints, for each pair of sequences, the percentage of identical positions. 

#Process bit 
for_range=list(range(0,len(input_seqs)))
#len_input_seqs=4
#range_len_input_seqs=(0,4)
#list(range_input_seqs)=[0,1,2,3]
for_range

#Need a loop for x and y accessions of pairwise comparison, just do all of them!

# "X axis" loop

for Xaxis_item in for_range:
#converting the first element of input_seqs into a list itself
	first_query=list(input_seqs[Xaxis_item]
#"Y" axis loop
	for Yaxis_item in for_range:
#Reset distance measure
	distance=0
	other_query=list(input_seqs[input_seqs[Yaxis_item])
#Go along each base in each of the two sequences to compare if identical or not. Score +1 if it is.
	for base in list(range(0, len(first_query))):
		print("Index"+str(base)+":"+
		str(first_query[base]+","+str(other_query[base]+"...")
		if first_query[base]==other_query[base]:
			distance=distance+1
#Output pairwise comparison done, output details
#Dont include the self comparison in the summary output
		if input_seqs[Xaxis_item] != input_seqs[Yaxis_item]:
			print(str(distance)+" identities between " + input_seqs[Xaxis_item] + " and " + input_seqs[Yaxis_item])
			print("\t" + str(int(100*(distance/len(input_seqs[Xaxis_item])))) + " percent similarity between " + input_seqs[Xaxis_item] + " and " + input_seqs[Yaxis_item])


