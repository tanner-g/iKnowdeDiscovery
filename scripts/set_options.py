#set_options.py will print and handle options based on filesystem type
import os

def read_params():
    filesystem_type = open("/usr/tmp/iKnowdeDiscovery/ext_type", "r")
    ext_option = filesystem_type.readline()

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

def ext_2():
    print(" OPTIONS for EXT 2 will go here")
    os.system("./option_ext2.sh")
def ext_3():
    print(" OPTIONS for EXT 3 will go here")
    os.system("./option_ext3.sh")
def ext_4():
    print("OPTIONS FOR EXT 4 will go here")
    os.system("./option_ext3.sh")


read_params()
