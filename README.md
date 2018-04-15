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

##

### ![#1589F0] Files

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

- **welcome.sh**
  - script to print ASCII art and welcome message to the user
  - Below ASCII banner will display options menu for user to select
  
- **clean_up.sh**
  - removes temporary files created by iKnowdeDiscovery tool

- **print_line.sh**
  - script prints dashed line separator based on welcome banner length
  - helps creating visual separation between commands and tool output for user

##

#### PROJECT REMINDER

 - When contributing to the project, make sure to **PULL** before you **PUSH**

##
