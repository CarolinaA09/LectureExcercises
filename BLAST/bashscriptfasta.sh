#!/bin/bash
 
while read Q_acc S_acc pc_identity alignment_length mismatches gap_opens Q_start Q_end S_start S_end evalue bitscore
	do
	echo -e $Q_acc\t$S_acc
done < HSP_lines_only.out
	
