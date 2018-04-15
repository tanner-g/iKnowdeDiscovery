# Script used to get ext filesytem information
#! /bin/bash


# Checking if the filesystem is either in ext2 or ext3/4
echo [COMMAND] sudo file -s $filesystempath
filesysteminfo=$(sudo file -s $filesystempath > user_path)
python ext_detect.py < user_path_test
