import sys

extcommandresult = ""
filename = "/usr/tmp/iKnowdeDiscovery/ext_type"
outputFile = open(filename, 'w')
# user_path = file path typed by user
filename2 = "/usr/tmp/iKnowdeDiscovery/user_path"
outputFile2 = open(filename2, 'w')
usertypedpath = ""

for line in sys.stdin:
    extcommandresult = line
    usertypedpath = line[0:line.find(":")]
    outputFile2.write(usertypedpath) 
if (extcommandresult.find("ext2") != -1): 
    print("EXT2")
    outputFile.write("EXT2")
elif (extcommandresult.find("ext3")) != -1:
    print("EXT3")
    outputFile.write("EXT3")
elif (extcommandresult.find("ext4")) != -1:
    print("EXT4")
    outputFile.write("EXT4")
else:
    print("ERROR")
    outputFile.write("ERROR")

outputFile.close()
outputFile2.close()
