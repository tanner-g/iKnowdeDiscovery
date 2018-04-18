# Script used to get ext filesytem information
#! /bin/bash


# Checking if the filesystem is either in ext2 or ext3/4
echo [COMMAND] sudo file -s $filesystempath
filesysteminfo=$(sudo file -s $filesystempath > /usr/tmp/iKnowdeDiscovery/user_path)
result=$(python ext_detect.py < /usr/tmp/iKnowdeDiscovery/user_path)

if [ "$result" == 'ERROR' ]
then
	echo "[ERROR] BAD FILESYSTEM TYPE"
elif [ "$result" == 'EXT2' ]
then
	echo "[OK] Filesytem type: EXT2"
elif [ "$result" = 'EXT3' ]
then
	echo "[OK] Filesystem type: EXT3"
elif [ "$result" == 'EXT4' ]
then
	echo "[OK] Filesystem type: EXT4"
else
	echo "[ERROR] NO FILESYSTEM TYPE DETECTED"
fi
