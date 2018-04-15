import sys

extcommandresult = ""

for line in sys.stdin:
    extcommandresult = line

if (extcommandresult.find("ext2") != -1): 
#and (systempath.find("ext3") or systempath.find("ext4"))):
    print("WE GOT ONE!!!")
    print(extcommandresult)
elif (extcommandresult.find("ext3") or extcommandresult.find("ext4")) != -1:
    print("FOUND EXT3/4 system: \n" + "RESULT:\t"+extcommandresult)
else:
    print("ERROR: BAD filesystem result\n" + extcommandresult)

