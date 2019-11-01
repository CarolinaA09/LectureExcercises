#!/bin/python

import os

#The fields are separated by commas (hence the "csv" suffix on the filename: csv stands for Comma Separated Values)
#Print out the gene names for all genes from the species Drosophila melanogaster or Drosophila simulans.
#Print out the gene names for all genes that are between 90 and 110 bases long.
#Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.
#Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.
#For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).

mosca3=open("data.csv") #archivo con una \n al final por eso se la quita con rstrip

#split() corta donde hay espacios, por eso si lo uso de esa manera corta el nombredel genero y el resto lo agrupa en la especie. 
#si lo uso asi tienes las separaciones que quieres, cada elemento separado por una coma pero el problema es que no lo tienes en diferentes lineas y lo peor de todo es que tienes esto '485\nDrosophila yakuba'

mosca_read=mosca3.read().rstrip().split("\n")
mosca_read #tienes toda la linea de nombre, sequencia, gen y expresion, separados de los demás pero aun no los tenes en diferentes lineas. Para eso ya toca usar un foor loop. 

for everyelement in mosca_read:
	everyelement=everyelement.split(",") #split makes a string into a list. It separated it by coma. The thing is how it distinguishes between everset. Is it because between is set there is a ""
#	print(everyelement)
	names=everyelement[0]
#	print(names)
	geneseqs=everyelement[1].upper()
#	print(geneseqs)
	seqlenghts=len(everyelement[1]) #now we learnt that each character of a string has its position. 
#	print(seqlenghts)	
	genenames=everyelement[2]
#	print(genenames)	
	expressionlevel=int(everyelement[3]) #has to make it an integer because it is a string
#	print(expressionlevel)
	ATcontent=(geneseqs.count('A')+geneseqs.count('T'))/(seqlenghts)
#	print(ATcontent)
	if 90 >= seqlenghts <= 100:
		print(genenames +  " has a lenght of  " + str(seqlenghts))
	if ATcontent < 0.65 and expressionlevel > 200:
		print(genenames + " has an AT content of " + str(ATcontent) + " and an expression level of " + str(expressionlevel))
	if ((genenames[0] == "k" or genenames[0] == "h")) and not names == "Drosophila melanogaster":
		print(genenames + " starts with k or h and are not Drosophila melanogaster")
	if ATcontent > 0.65:
		print(genenames + "has an AT content that is higher than 0.65")
	elif ATcontent < 0.45:
		print(genenames + "has an AT content that is less than 0.45")
	else: 
		print(genenames + "has an AT content between 0.45 and 0.65")
	
