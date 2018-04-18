#!/bin/bash
# Script used to get ext filesytem information

# Checking if the filesystem is either in ext2 or ext3/4
echo [COMMAND] sudo file -sL $filesystempath
filesysteminfo=$(sudo file -sL $filesystempath > /usr/tmp/iKnowdeDiscovery/full_user_path)
result=$(python ext_detect.py < /usr/tmp/iKnowdeDiscovery/full_user_path)

if [ "$result" == 'ERROR' ]
then
	echo "[ERROR] BAD FILESYSTEM TYPE"
elif [ "$result" == 'EXT2' ]
then
	echo "[MESSAGE] Filesytem type: EXT2"
elif [ "$result" = 'EXT3' ]
then
	echo "[MESSAGE] Filesystem type: EXT3"
elif [ "$result" == 'EXT4' ]
then
	echo "[MESSAGE] Filesystem type: EXT4"
else
	echo "[ERROR] NO FILESYSTEM TYPE DETECTED"
fi
