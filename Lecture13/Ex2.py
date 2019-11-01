#!/bin/python3

#Modify the function from the previous exercise above so that it accepts a list of amino acid residues rather than a single one, and count these within the protein sequence.
#If no list is given, the function should return the percentage of hydrophobic amino acid residues (i.e. amino acids A, I, L, M, F, W, Y, V).

aminoacid='AILMFWYV'

protein='MSRSLLLRFLLFLLLLPPLP'

def percentage_aminoacid(protein, AA = ["A", "I", "L", "M", "F", "W", "Y", "V"]):
        sequence=protein.upper()
        length=len(protein)
	counter=0
	for aminoacid in AA:
		aminoacid_counter = sequence.count(aminoacid.upper())
		counter = counter + aminoacid_counter	
        percentage=(counter/length)*100
        return percentage
	
