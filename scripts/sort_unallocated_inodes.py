import datetime
f = open("/usr/tmp/iKnowdeDiscovery/unallocated_inodes.txt", "r")
inodes = list()

for line in f:
    inode, time = line.strip().split(",")
    ntime = time[:19]
    date = datetime.datetime.strptime(ntime, "%Y-%m-%d %H:%M:%S")
    inodes.append([inode, date])
f.close()
sorted(inodes, key=lambda x: datetime.datetime.strftime(x[1], "%Y-%m-%d %H:%M:%S"))
f = open("report.txt", "a")
f.write("\nInodes recently unallocated:\n")
if len(inodes) == 0:
    f.write("  There were no recently freed inodes.")
else:
    for item in inodes:
        f.write("  " + item[0] + " -> " + datetime.datetime.strftime(item[1], "%Y-%m-%d %H:%M:%S") + "\n")
f.close()

