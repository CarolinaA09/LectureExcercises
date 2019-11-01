#!/bin/python3

#test:
#dna="abcdefghijk"

#window=6
#letters=0

#for letters in range(len(dna)-(window-1)):
#	print(dna[letters:letters+window])


#for real:
dna=open("exon_to_other_class.fasta").read().split()[1]

windowsize=30
offset=3

#for letters in range(len(dna)-(window-1))
#	segment=dna[letters:letters+window]
#	letters=letters+offset
#	segment
#	fasta_file_name="AJ223353" + "letter_" + str(letters) + "offset_" + str(offset)
#	fasta_header=">AJ223353" + "letter_" + str(letters) + "offset_" + str(offset) 
#	new_files=open(fasta_file_name + ".fasta", "w")
#	new_files.write(fasta_header + "\n")
#	new_files.write(segment)
#	new_files.close()
#	letters=letters+offset

#he is creating a list with all the numbers from 0 to three hundred and something to move in de sequences
segment_starts=list(range(0,len(dna),offset))
segment_starts

#Create and then close a file object to take all segnment sequences

basic_fasta_header="_window"+str(windowsize) + '_offset' + str(offset)
alloutfilename='AJ223353_coding_all' + basic_fasta_header + '.fasta'
allsegments=open(alloutfilename, 'w')
allsegments.write('')
allsegments.close()

#create a blank list to hold the segnments
segments_made=[]

#create a possible yes/no switching variable, i.e conditional
fileswanted=1

#the for loop
for seg_bits in segment_starts:
	tempseq=dna[seg_bits:seg_bits+windowsize].upper() # it will be 0 + 0+30, then 1 + 1+30
#	tempseq
	segments_made=segments_made+[tempseq] #he is saving the segnments in a list
#	segments_made	
	tempGC=int(100*((tempseq.count("G") + tempseq.count("C"))/(len(tempseq)))) #calculating the GC contente
#	tempGC
	descriptionline='AJ223353_coding_' + str(len(segments_made)) + '_' + tempseq+basic_fasta_header
#	descriptionline   	
	fastaheader='>' + descriptionline
#	fastaheader
	if fileswanted == 0:
		print(len(segments_made),'\t',tempseq,'\t',tempGC)	
#Do we want files written? Answer will be either True or False (maybe NOT is not an option)
	elif fileswanted == 1:
		segmentfile = open(descriptionline+'.fasta', 'w') #creating files for each segment
		allsegments = open(alloutfilename, 'a') #one single file for each segment that is why he is only appending the file
		segmentfile.write(fastaheader+'\n'+tempseq)
       		allsegments.write(fastaheader+'\n'+tempseq+'\n\n')
		segmentfile.close()
		allsegments.close()

#outside the loop, print the first 10 segments, one per line:
print('\n'.join(segments_made[0:10]))

#Print the first 3 segments, separated by the word 'then'
print(' then '.join(segments_made[0:3]))

#the combined fasta file doesnt looks good, with foor loop it gets the correct format

new_file_fasta=open(alloutfilename)
for line in new_file_fasta:
	first=line.rstrip('\n\n') #it is not working 
	print(first)









