sequence="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

print(sequence)

replacement1=sequence.replace("A",t)
replacement2=sequence.replace("C",g)
replacement3=sequence.replace("T",a)
replacement4=sequence.replace("G",c)

print("The complement sequence of sequence is", str(replacement4.upper()))

genomic=ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

motif=genomic.find("GAATTC")--> give the position of the string [34:40]
print(motif)
