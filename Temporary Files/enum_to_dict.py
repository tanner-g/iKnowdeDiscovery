import os

path = "/usr/tmp/iKnowdeDiscovery/enum/"

dictionaries = []

for data_file in os.listdir(path):
	with open(os.path.join(path,data_file)) as file_pp:
		file_dict = {}
		first_line = True
		files = []
		inode = 0
		for line in file_pp:
			if first_line:
				first_line = False
			else:
				if line:
					tmp = line.strip("\n").split("\t")
					files.append(tmp[1])
					if inode == 0:
						inode = tmp[0]
		file_dict[inode] = files
		dictionaries.append(file_dict)
		inode = 0
		files = []
		file_dict = {}
print(dictionaries)

			

