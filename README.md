# iKnowdeDiscovery
 

## Background

iKnowdeDiscovery is an open source tool that enhances inode history and tracking by creating a user friendly visualization of a system's inode timelime. We strive to make inode information more meaningful to forensic investigators by making it easier to track, parse, and visualize data attached to an inode.


### Features

 - **Detect suspicious Inode Activity**
   - Detect, log, and show recently freed/created/altered Inodes
 - **Inode Tree Visualizer**
   - Using Python's PLOTLY to show Inodes on a graph
 - **Hardlink File Detection**
   - Detect multiple files that point to the same Inode

### Files

- **enumeration.sh**
  - Enumerates all files in a directory
  - Get the Inode of each file
  - Find all other files with each of those inodes

##
#### PROJECT REMINDER

 - When contributing to the project, make sure to **PULL** before you **PUSH**
##
