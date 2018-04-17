if "Not Allocated" in open("/usr/tmp/iKnowdeDiscovery/inode_alloc_result.txt").read():
    f = open("/usr/tmp/iKnowdeDiscovery/inode_alloc_result.txt", "r")
    fi = open("/usr/tmp/iKnowdeDiscovery/unallocated_inodes.txt", "a")
    for line in f:
        if "inode:" in line:
            inode = line.strip().split(" ")[1]
        if "Inode Modified" in line:
            beginning, date = line.strip().split("\t")
            if date[0] != "0":
                fi.write(inode + "," + date + "\n")
