# main.sh
# Description: main.sh runs the main body of the program and calls supporting scripts for necessary features
#! /bin/bash

# Displays welcome message/ascii art
sh ./welcome.sh

# Filesystem prompt
# Once filesytem is specified, script checks for filesystem type
echo -e 'Please type a filesystem path, [ Example: /dev/sda1 ]'
echo 'Then press [ENTER]'
# once we know if its ext2 or ext3/4 we can display the options that are available for that type

read filesystempath

echo $filesystempath
