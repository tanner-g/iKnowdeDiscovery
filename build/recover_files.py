#this will recover "Deleted" files if possible from the EXT2 system
import os
f = open("/usr/tmp/iKnowdeDiscovery/unallocated_blocks.txt", "r")
first_line = True
for line in f:
    if (first_line):
        partition = line.strip()
        first_line = False
    else:
        inode, block = line.strip().split(",")
        if " " in block:
            blocks = block.split(" ")
            print(blocks)
        else:
            blocks = block
            print(blocks)
            #output = 
