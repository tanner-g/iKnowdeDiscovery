#!/bin/bash
partition=$1
filesystem=$2
iter=5 #541000
touch /usr/tmp/iKnowdeDiscovery/unallocated_inodes.txt
while [ $iter -le 200 ] #543000 ]
do
	sudo istat $partition $iter > /usr/tmp/iKnowdeDiscovery/inode_alloc_result.txt		
	python find_unallocated_inodes.py
((iter++))
done

python sort_unallocated_inodes.py
