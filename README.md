# iKnowdeDiscovery
 

## Background

**iKnowdeDiscovery** is an open source tool that simplifies inode forensic analysis. We strive to make inode information more meaningful and comprehensible to the forensic community by making it easier to track, parse, and visualize data attached to an inode.

##
### Running the Tool
```
cd /iKnowdeDiscovery/build/
./main.sh

```
##
### Features

 - **Hardlink File Detection**
   - Detect multiple files that point to the same Inode
 - **Detect suspicious Inode Activity**
   - Detect, log, and show recently freed/created/altered Inodes
 - **Inode Tree Visualizer**
   - Use Python's PLOTLY to show Inodes on a graph
##

### Files  

- **main.sh**
  - Calls the welcome page
  - Displays to functions available to user within the tool
  - Calls support functions based on the user's command line input

- **enumeration.sh**
  - Enumerates all files in a directory
  - Get the Inode of each file
  - Find all other files with each of those inodes

- **ext_detection.sh**
  - Reads in user path and runs file command on that path
  - Passes output of the file command to Python script **ext_detect.py** for analysis

- **ext_detect.py**
   -  script parses output and sends status code based on ouput

  - Status Codes:
    - EXT2  &nbsp;&nbsp;&nbsp;--> &nbsp;&nbsp;Detects an EXT2 Filesystem
    - EXT3  &nbsp;&nbsp;&nbsp;--> &nbsp;&nbsp;Detects an EXT3 Filesystem
    - EXT4  &nbsp;&nbsp;&nbsp;--> &nbsp;&nbsp;Detects an EXT4 Filesystem
    - ERROR&nbsp;&nbsp;&nbsp;--> &nbsp;&nbsp;No file system detected

##

#### PROJECT REMINDER

 - When contributing to the project, make sure to **PULL** before you **PUSH**

##
