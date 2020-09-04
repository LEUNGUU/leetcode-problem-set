#!/bin/bash


function print() {
filename=($(ls $1 | sort -n))

# loop over all the files based on the numeric order
for file in "${filename[@]}";
do
	cat $1$file >> print
	echo -e "\n-------------------------------------------------------------------------------\n" >> print
done

}


print $@
# Printout to pdf
enscript -1rG -B  --highlight=python --font=Courier@10 --margins=10:10:5:5 -p - --color=1 print | pstopdf -i -o out.pdf
