if "Not Allocated" in open("/usr/tmp/iKnowdeDiscovery/inode_alloc_result.txt").read():
    f = open("/usr/tmp/iKnowdeDiscovery/inode_alloc_result.txt", "r")
    fi = open("/usr/tmp/iKnowdeDiscovery/unallocated_inodes.txt", "a")
    nf = open("/usr/tmp/iKnowdeDiscovery/unallocated_blocks.txt", "a")
    deleted = False
    blocks_next_line = False
    i = False
    for line in f:
        if "inode:" in line:
            inode = line.strip().split(" ")[1]
        elif "Inode Modified" in line:
            beginning, date = line.strip().split("\t")
            if date[0] == "0":
                fi.write(inode + "," + date + "\n")
        elif "links" in line:
            cond, links = line.strip().split(": ")
            if (links != "0"):
                    deleted = True
        elif "Direct Blocks:" in line:
            blocks_next_line = True

        curr = line
    if (blocks_next_line and deleted):
        if curr.strip() != "Direct Blocks:":
            blocks = line.strip()
            nf.write(inode + "," + blocks + "\n")
    f.close()
    fi.close()
    nf.close()
