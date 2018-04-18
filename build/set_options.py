# set_options.py will print and handle options based on filesystem type
import os

#filesystempath = ""     # filesytempath = full path for filesystem partition
#ext_option = ""         # ext_option = file system type determined by script

def read_params():
    filesystem_type = open("/usr/tmp/iKnowdeDiscovery/ext_type", "r")
    ext_option = filesystem_type.readline()
    filesystem_path = open("/usr/tmp/iKnowdeDiscovery/user_path", "r")
    filesystempath = filesystem_path.readline()

    filesystem_path.close()
    filesystem_type.close()

    # check user's filesystem type: health check
    system_check(ext_option, filesystempath)

def ext_2_print():
    print("(1) Hardlink Visualizer")
    print("(2) xxx")
    print("(3) xxx")
    print("(4) xxx")
    print("(5) xxx")

def ext_3_print():
    print("(1) Hardlink Visualizer")
    print("(2) xxx")
    print("(3) xxx")
    print("(4) xxx")
    print("(5) xxx")

def ext_4_print():
    print("(1) Hardlink Visualizer")
    print("(2) xxx")
    print("(3) xxx")
    print("(4) xxx")
    print("(5) xxx")

def system_check(ext_option, filesystempath):
# testing --> ext option value
    print("CHECKING: "+ ext_option)
    if ext_option == "EXT2":
        ext_2_print()
        user_prompt()
    elif ext_option == "EXT3":
        ext_3_print()
        user_prompt()
    elif ext_option == "EXT4":
        ext_4_print()
        user_prompt()
    else:
        print("[ERROR]  No options available for your filesystem type")
        exit_program()

def user_prompt():
    userInput = str(raw_input("[PROMPT] Enter an option [Exit(e)]: "))
    print("You entered: " + userInput)
    userInput2 = str(raw_input("Is that correct? [Y(y) / N(n)]: "))
    if userInput == "e":
        exit_program()    
    elif (userInput2 == "Y") or (userInput2 == "y"):
        if userInput == "1":
            run_enumeration()
            print("Enumeration Worked!!!")
            user_prompt()       
        elif userInput == "2":
            print("You choose option 2")
            user_prompt()
        elif userInput == "3":
            print("you choose option 3")
            user_prompt()
        else:
            print("[ERROR] Invalid Selection")
            user_prompt()
    else:
        print("[MESSAGE] Ok, Re-Entering User Prompt")
        user_prompt()
        

def run_enumeration():
    userInput3 = str(raw_input("[PROMPT} Enter a full directory path: "))
    os.system("sudo ./enumeration.sh " + str(filesystempath) + " " +userInput3)
    # testing
    os.system("sudo python ../'Temporary Files'/enum_to_dict.py")
    user_prompt()

def exit_program():
    os.system("./print_line.sh")
    print("[MESSAGE] Program Terminated")
    os.system("./print_line.sh")


# start of script reads parameters, determine filesytem attributes
read_params()


