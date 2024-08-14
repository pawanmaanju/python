import os

# Specify the directory path
path = '/bin'

# Get the list of all files and directories
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
print(dir_list)