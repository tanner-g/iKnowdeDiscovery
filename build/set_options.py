# set_options.py will print and handle options based on filesystem type
import os
import sys

#filesystempath = ""     # filesytempath = full path for filesystem partition
#ext_option = ""         # ext_option = file system type determined by script

def read_params():
    filesystem_type = open("/usr/tmp/iKnowdeDiscovery/ext_type", "r")
    ext_option = filesystem_type.readline()
    filesystem_path = open("/usr/tmp/iKnowdeDiscovery/user_path", "r")
    filesystempath = filesystem_path.readline()

    filesystem_path.close()
    filesystem_type.close()
    
    # runs tool menu prompt loop
    user_prompt(ext_option, filesystempath)

def ext_2_print():
    print("(1) Hardlink Visualizer")
    print("(2) Inode Analysis")

def ext_3_print():
    print("(1) Hardlink Visualizer")
    print("(2) Inode Analysis")
    print("(3) Find Orphan Nodes")

def ext_4_print():
    print("(1) Hardlink Visualizer")
    print("(2) Inode Analysis")
    print("(3) Find Orphan Nodes")

def system_check(ext_option, filesystempath):
    if ext_option == "EXT2":
        ext_2_print()
    elif ext_option == "EXT3":
        ext_3_print()
    elif ext_option == "EXT4":
        ext_4_print()
    else:
        print("[ERROR]  No options available for your filesystem type")
        exit_program()

def user_prompt(ext_option, filesystempath):
    system_check(ext_option, filesystempath)
    userInput = str(raw_input("[PROMPT] Enter an option [Exit(e)]: "))
    print("[USER INPUT] You entered: " + userInput)
    userInput2 = str(raw_input("[USER INPUT] Is that correct? [Y(y) / N(n)]: "))
    if userInput == "e":
        exit_program()    
    elif (userInput2 == "Y") or (userInput2 == "y"):
        if userInput == "1":
            print("[MESSAGE] Hardlink Visualizer Selected")
            run_enumeration(ext_option, filesystempath)
# testing
            print("Enumeration Worked!!!")
            user_prompt(ext_option, filesystempath)       
        elif userInput == "2":
            print("[MESSAGE] Inode Analysis Selected")
            print("[MESSAGE] Analyzing... Please wait...")
            os.system("sudo ./inode.sh " + filesystempath + " " + ext_option)
            user_prompt(ext_option, filesystempath)
        elif userInput == "3":
            if ext_option == "EXT3" or ext_option == "EXT4":
                print("[MESSAGE] Find Orphan Nodes Selected")
                os.system("sudo ./orphanNodes.sh " + filesystempath)
                user_prompt(ext_option, filesystempath)     
            else:
                print("[ERROR] Bad Selection")
                user_prompt(ext_option, filesystempath)
        else:
            print("[ERROR] Invalid Selection")
            user_prompt(ext_option, filesystempath)
    else:
        print("[MESSAGE] Ok, Re-Entering User Prompt")
        user_prompt(ext_option, filesystempath)
        

def run_enumeration(ext_option, filesystempath):
    userInput3 = str(raw_input("[PROMPT} Enter a full directory path: "))
    os.system("sudo ./enumeration.sh " + str(filesystempath) + " " +userInput3)
    # testing
    os.system("sudo python ../'Temporary Files'/enum_to_dict.py")
    user_prompt(ext_option, filesystempath)

def exit_program():
    os.system("./print_line.sh")
    print("[MESSAGE] Program Terminated")
    os.system("./print_line.sh")
    sys.exit()

# start of script reads parameters, determine filesytem attributes
read_params()


