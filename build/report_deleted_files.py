f = open("/usr/tmp/iKnowdeDiscovery/deleted_files.txt", "r")
r = open("report.txt", "a")
r.write("\nFiles deleted from system:\n")
count = 0
for line in f:
    if ( count <= 1000 ):
        inodeandfile = line.strip().split(" * ")[1]
        inode, filename = inodeandfile.split(":")
        inode.strip()
        filename.strip(" \t")
        r.write("  " + inode + " -> " + filename + "\n")
    count += 1
f.close()
r.close()
