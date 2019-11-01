
#!/usr/bin

unser IFS
IFS=$'\t'
count=0
while read subject_acc. %_identity alignment_length  
do 
count=$((count+1))
echo -e "$count\t$subject_acc. $%_identity $alignment_length"
done < blastoutput2.out | head -10

while read mismatches
do
if test -z $mismatches || test $mismatches == mismatches
 then
 continue
 else
 count=$((count+1))
  if test $mismatches -eq  20
   then outfile=$mismatches.details
 fi
echo -e "$mismatches" >>$outfile3 
fi
done < blastoutput2.out | head -10

while read alignment_length mismatches
do 
if test -z $alignment_length || test $alignment_length == alignment_length
 then
 continue
 else
 count=$((count+1))
  if test $alignment_length -ls 100
   then outfile3.1=$
 fi
echo -e "$mismatches" >>$outfile3
fi
done < blastoutput2.out | head -10

