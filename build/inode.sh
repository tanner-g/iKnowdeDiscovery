#!/bin/bash
partition=$1
filesystem=$2
iter=5 #541000
touch /usr/tmp/iKnowdeDiscovery/unallocated_blocks.txt
touch /usr/tmp/iKnowdeDiscovery/unallocated_inodes.txt
if [ $filesystem == "EXT2" ]; then
	mkdir recovered_files
fi
while [ $iter -le 200 ] #543000 ]
do
	sudo istat $partition $iter > /usr/tmp/iKnowdeDiscovery/inode_alloc_result.txt		
	python find_unallocated_inodes.py
((iter++))
done
if [ $filesystem == "EXT2" ]; then
	python recover_files.py
fi
sudo fls /dev/mapper/fedora-root 2 #/dev/sdb 2

python sort_unallocated_inodes.py
