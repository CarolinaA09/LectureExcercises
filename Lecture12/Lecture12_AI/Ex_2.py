#!/bin/python

#Make our input_seq into one big long string, then compare all bases against all bases.

import os

input_seqs=['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

s=""

myseqs=s.join(str(e) for e in input_seqs) #we want to take each element e of the list, and for each element in list, join it as a string to the next one with separator s

myseqs

#Generate a table to put values: a 2 dimensional "numpy" table

#To do this we need the numpy module

import numpy as np

#we need a rank 2 array with 2 rows and 3 columns

a=np.array([[1,2,3],[4,5,6]])

#shape of the array
print(a.shape)
print(a)

#Create a 12 by 4 array of all zeros

b=np.zeros((12,4))

print(b)

#Create a 5 by 2 array of all ones
c=np.ones((5,2))
print(c)

d=np.full((3,2),6)
print(d)

#Create a 2 by 2 array filles with random (floating point) values
e=np.random.random((2,2))
print(e)

#Indexes start at zero, remember!
e[1,1]

#Create a 3 by 3 identity matrix
f=np.eye(3)

####################################USING TABLES FOR SEQUENCES SIMILARITIES
myseqs
len(myseqs)


#Using an identity matrix because it is the closes to what we are trying to do

IDmatrix=np.eye(len(myseqs))
print(IDmatrix)

#Now, all we need is 2 for loops to iterate over the X-axis and Y-axis
#We will traeat the rows as X and Y columns
#We will be doing 36x36(1296) base-base comparisons because the len of the dna seq is 36

#a human counter for the x base position: xcounter and ycounter
#the for loops

xcounter=0 #this will only count the first then the second base then the third base etc. 
for xbase in myseqs:
	xcounter=xcounter+1 #here it enters zero (so it will be the first base) but next time it will be 1, next time it will be 2 etc. until 36. So each  base of the piece of DNA are runned agains all 36 bases 
	ycounter=0
	for ybase in myseqs:
		ycounter=ycounter+1 #this is the counter that will show that all 36 bases is compared against 1
#		print(xcounter,ycounter,xbase,ybase)
		if ybase==xbase:
			IDmatrix[(xcounter-1),(ycounter-1)]=1 #le estan restando uno por el hecho de que el counter entro como 1 a ese loop y la primera posicion es 0. 
			print(IDmatrix)
		

#Print out the array we have populated (rows,columns)
#Firs row only
len(IDmatrix[0,]) #it will be 36
IDmatrix[0,] #will print the first row of the matrix

#First row only, which ones were identical to the first base of my seqs
IDmatrix[0,]>0 #will output a matrix of true/false and every time there is a 1 or a match with the first dna base, there will be a a True. 

#first9 compared to first 9
print(IDmatrix[0:9,0:9])

#this time first 9 compared to second 9
print(IDmatrix[0:9,9:18])

#We want the "equivalent position" values, which is the diagonal
IDmatrix[0:9,9:19].diagonal() #why is it 19????

#We can process the values in the diagonal
IDmatrix[0:9,9:18].diagonal().sum()

#Make it a percentage
print("The similarity was",int((IDmatrix[0:9,9:18].diagonal().sum()/9)*100),"percent")











