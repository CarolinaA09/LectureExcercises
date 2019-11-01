#!/bin/python

input=open('input.txt')

sliced_pieces=[]

for sequence in input:
	sliced=input[14:]
	sliced_pieces.append(sliced)

new_file = open('output.txt', 'w')
new_file.write('\n'.join(sliced_pieces))
new_file.close()
	
