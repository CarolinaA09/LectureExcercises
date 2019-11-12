#!/usr/bin/python3


#Files are available from /localdisk/data/BPSM/Lecture17_AI/, but I would recommend that you update the eukaryotes.txt file with the latest version from NCBI.

#Use a pandas dataframe to address the following questions:
#how many fungal species have genomes bigger than 100Mb? What are their names?
#how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
#which Heliconius species genomes have been sequenced?
#which sequencing centre has sequenced the most plant genomes? the most insect genomes?
#add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?
#draw a vertical bar plot which shows the number of genes, number of proteins, and number of genes per protein for all genomes with at least twice as many proteins as genes. Use the secondary_y argument to display the number of genes per protein on a different y axis.

#import libraries
#import everything since the begenning, as many as you can. 

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Get the file 

os.system("wget -O eukaryotes.tsv 'ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt'")

#Read the file into a data frame:

df=pd.read_csv('eukaryotes.tsv', sep="\t",na_values=['-'])

print(df)

#how many fungl species have genmes biger than 100Mb?
#use two conditions joined with &

df.shape
df.columns #this will give me the index
list(df.columns)
df[3:7]
df.describe()

#Re-read the file in. telling pandas about mising data

df = pd.read_csv('/localdisk/data/BPSM/Lecture17_AI/eukaryotes.txt', sep="\t", na_values=['-'])
df.describe()

#to only see one of the columns

df['#Organism/Name'] #the result of doing this is a series

#put the more common at the top an cout values?
df['#Organism/Name'].value_counts()

#if we give a list of column of names instead of a single one then we get back a dataframe object.
df[['#Organism/Name', 'Size (Mb)', 'GC%']].head()

#to figure our which rows satisfy some condition, we can use a special shorthand:

df['#Organism/Name'] == 'Arabidopsis thaliana'

#Question 1:

len(df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)])
#86

#what are their names:
st(big_fungi['#Organism/Name'])

#this will only give you list(big_fungi) the list of th headers.

#this is just the sortder list



#Sizes of all the Thaliana genome df[df['#Organism/Name']=='Arabidopsis thaliana']['Size (Mb)']

sorted(list(big_fungi['#Organism/Name']))

#how many of each Kindom/group (plants, animals, ungi and protist) have been sequences?

#for one single group:
len(df[df['Group'] == 'Plants'])

#use a normal loop


