#set_options.py will print and handle options based on filesystem type
import os

filesystempath = ""

def read_params():
    filesystem_type = open("/usr/tmp/iKnowdeDiscovery/ext_type", "r")
    ext_option = filesystem_type.readline()
    filesystem_path = open("/usr/tmp/iKnowdeDiscovery/user_path", "r")
    filesystempath = filesystem_path.readline()
    filesystem_path.close()

    if ext_option == "EXT2":
        ext_2()
    elif ext_option == "EXT3":
        ext_3()
    elif ext_option == "EXT4":
        ext_4()
    else:
        print("[ERROR]  NO OPTIONS AVAILABLE")
        print("--- P R O G R A M --- T E R M I N A T I N G ---")
        os.system("./print_line.sh")
    filesystem_type.close()

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

def user_prompt():
    userInput = str(raw_input("[PROMPT] Enter an option [Exit(e)]: "))
    print("You entered: " + userInput)
    userInput2 = str(raw_input("Is that correct? [Y(y) / N(n)]: "))
    if userInput == "e":
        exit_program()    
    elif (userInput2 == "Y") or (userInput2 == "y"):
        if userInput == "1":
            run_enumeration()
            print("your back here")
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
        
   

def ext_2():
    ext_2_print()
    ext_2()

def ext_3():
    print(" OPTIONS for EXT 3 will go here")
   # os.system("./option_ext3.sh")

def ext_4():
    ext_4_print()
    user_prompt()

def run_enumeration():
    userInput3 = str(raw_input("[PROMPT} Enter a full directory path: "))
    os.system("sudo ./enumeration.sh " + str(filesystempath) + " " +userInput3)
    # testing
    os.system("sudo python ../'Temporary Files'/enum_to_dict.py")
    user_prompt()

def exit_program():
    os.system("./print_line.sh")
    os.system("[MESSAGE] Program Terminated by User")
    os.system("./print_line.sh")

read_params()
