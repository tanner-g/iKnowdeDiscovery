# main.sh
# Description: main.sh runs the main body of the program and calls supporting scripts for necessary features
#! /bin/bash

# Displays welcome message/ascii art
sh ./welcome.sh

# Filesystem prompt
# Once filesytem is specified, script checks for filesystem type
echo -e 'Please type a filesystem path, [ Example: /dev/sda1 ], then press [ENTER]'
# once we know if its ext2 or ext3/4 we can display the options that are available for that type

# Adds a line to split up text on screen
sh ./print_line.sh

# reads user input for path
read filesystempath
# export makes variable global in scope
export filesystempath
sh ./print_line.sh

# makes tmp iKnowdeDisovery directory
mkdir -p /usr/tmp/iKnowdeDiscovery/
chmod 755 /usr/tmp/iKnowdeDiscovery/

# ext_detection.sh checks the filesystem type
sh ./ext_detection.sh

# adds more visual separation between commands
sh print_line.sh

# Once filesystem is detected, suboptions can be printed
python set_options.py


# cleans up temp. files made by subroutines in the tool
sh ./clean_up.sh



# DONE./inode.sh <partition_path> <partition_type> (for EXT2/3/4)
#./orphanNodes.sh <partition_path> (for EXT3/4 only)
# DONE#./enumeration.sh <partition_path> <directory path> //need to in main ask user for path [ext2/3/4]
