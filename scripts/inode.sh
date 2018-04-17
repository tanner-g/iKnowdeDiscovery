#!/bin/bash
partition=/dev/mapper/fedora-root
filesystem=ext2
iter=2

while [ $iter -le 15 ]
do
	sudo istat $partition $iter > /usr/tmp/iKnowdeDiscovery/inode_alloc_result.txt		
	python allocated_ext34.py
	python allocated_ext34.py
((iter++))
done
python sort_unallocated_inodes.py
