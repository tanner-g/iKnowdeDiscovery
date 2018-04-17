from subprocess import call
partition = "/dev/mapper/fedora-root"
file1 = open('/usr/tmp/iKnowdeDiscovery/fsstat.txt', 'r')
inodes = list()
for line in file1:
    if "Orphan" in line:
        line.strip()
        entries = line.split(" ")
        for entry in entries:
            if entry != "Orphan" and entry != "Inodes:":
                inodes.append(entry.strip(","))
inodes.pop()
file1.close()
f = open("report.txt", "w")
f.write("Inodes associated with open files pending deletion:  \n")
for entry in inodes:
    res = call(["./ffindInode.sh", partition, entry])
    #f.write(entry + ",")
f.close()
