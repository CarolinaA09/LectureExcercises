#!/bin/bash


split -l 9940 Test_dataset.fa split_reads_directory/
ls - split_reads_directory/

ls | cat -n | while read n f 
do 
cp "$f" "reads -$n"
done

myfavoritesequence=ACATAAAACATCAAAGTGAACAGATTGTAGTGTAAGAAGTTAGATTAA


