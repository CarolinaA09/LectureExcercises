#!/usr/bin bash

rm -f*.exercise.out

grep -v "#" blastoutput2.out > HSP_lines_only.out 

inputfile=HSP_lines_only.out


