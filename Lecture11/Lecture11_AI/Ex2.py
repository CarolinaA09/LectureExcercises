#!/usr/bin/python

#Programme to trim fixed lenght adapter sequences from start of each sequence
#and keep the output in a file, outputting to screen as we go.

#Open and read the file, trimming off adapter on the fly
import os

input_txt_contents_file=open('input.txt').read().split() #split eliminated the \n and made a list out of all the sequences separated by comas.

input_txt_contents_file #checking the file

len(input_txt_contents_file)

#create a file where I am putting the sequences without an adaptor:
adaptor_removed_seq=open("cleansequences.txt", "w")

for every_element in input_txt_contents_file:
	adaptor_removed_seq.write(every_element[14:] + "\n") #everytime writting on the file the new trimmed sequences line by line
	every_element[14:] #seeing the trimmed sequences. I am eliminating the first part

adaptor_removed_seq.close()
print(open("cleansequences.txt").read().rstrip()) #se incluye la ultima rstrip porque hay un "\n" dn la ultima linea del archivo por el loop. 


	









