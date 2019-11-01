#!/bin/python3

#What is requiredWrite a script/programme which creates nine new 'size range' directories, one for sequences between 100 and 199 bases long, one for sequences between 200 and 299 bases long, etc., etc..Chose one of the .dna files as an input file, and write out each DNA sequence in that input file to a separate file in the appropriate 'size range' directory.

#In metagenomics, binning is the process of grouping reads or contigs and assigning them to operational taxonomic units. Binning methods can be based on either compositional features or alignment (similarity), or both.


#Start python

import os,sys,shutil

#moved the sequences using unix to a nex file.

#Get a list of the files we might want to process
#We need tha path: directory and the file name.

#creating a variable that works as a sequence identifier number o just a sequence counter
seq_number=1

#This loop would open each file.
for file_name in os.listdir('dna_files/'): #we are running it from the master directory
	if file_name.endswith('.dna'):
		print('Reading sequences from ' + file_name)
		dna_file=open('dna_files/' + file_name) #openning each file
#This loop then looks at each line and gets the lenght
		for line in dna_file:
			dna=line.rstrip('\n') #file has sequences in different lines so we are stripping them
			length=len(dna) #calculating the lenght of each line
			print('\tsequence length is ' + str(length)) #Getting each size bin to see if sequences fits a certain range.
			for bin_lower in list(range(100,1000,100)): #Go through each bin and check if the sequence belongs in it. Created a range from a 100 to 1000 that jumps in 100. It should compare each sequence lenght to all the numbers in the range. 
				bin_upper=bin_lower + 99
#				bin_directory_name = str(bin_lower) + '_' + str(bin_upper) #He firs use this to create directories
#				shutil.rmtree(bin_directory_name) #removing any previos files from past runs
#				os.mkdir(bin_directory_name) #re-creating the directories #He created those directories
				if length >= bin_lower and length <= bin_upper: #checking the size of the sequences in the lenght
					print('\t\tbin is ' + str(bin_lower) + ' to ' + str(bin_upper))
					bin_directory_name = str(bin_lower) + '_' + str(bin_upper)
					output_path=bin_directory_name + '/' + str(seq_number) + '.dna' #creating a path that leads to a file
					output=open(output_path, "w") #creating the file based on the path
					output.write(dna) #writting the dna in the file
					output.close()
					seq_number=seq_number+1 #sequence counter for the name of the new files that are in the new directory.
									

						
