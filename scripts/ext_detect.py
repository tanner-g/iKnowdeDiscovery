import sys

extcommandresult = ""

for line in sys.stdin:
    extcommandresult = line

if (extcommandresult.find("ext2") != -1): 
#and (systempath.find("ext3") or systempath.find("ext4"))):
    print("EXT2")
elif (extcommandresult.find("ext3")) != -1:
    print("EXT3")
elif (extcommandresult.find("ext4")) != -1:
    print("EXT4")
else:
    print("ERROR")
