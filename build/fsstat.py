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
if (len(inodes) != 0):
    inodes.pop()
file1.close()
f = open("report.txt", "w")
f.write("Inodes associated with open files pending deletion:  \n")
if (len(inodes) == 0):
    f.write("  No current orphan inodes.")
else:
    for entry in inodes:
        res = call(["./ffindInode.sh", partition, entry])
f.close()
