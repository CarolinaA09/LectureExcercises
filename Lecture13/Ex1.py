#!/bin/python3

#Write a function that takes two arguments (a protein sequence and an amino acid residue code) and returns the percentage of the protein that the amino acid makes up.

#Once you have written a function, use the following assertions to test your function:


protein='MSRSLLLRFLLFLLLLPPLP'

length=len(protein)

M_protein=protein.upper().count('M')
print(M_protein)

S_protein=protein.upper().count('S')
print(S_protein)

R_protein=protein.upper().count('R')
print(R_protein)

L_protein=protein.upper().count('L')
print(L_protein)

F_protein=protein.upper().count('F')
print(F_protein)


def percentage_aminoacid(protein, AA):
	sequence=protein.upper().count(AA.upper())
	length=len(protein)
	percentage=(sequence/length)*100
	return percentage

assert round(percentage_aminoacid("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(percentage_aminoacid("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(percentage_aminoacid("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(percentage_aminoacid("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)



