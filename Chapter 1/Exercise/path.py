import os  # Importing the 'os' module to interact with the operating system

# Specify the directory path (in this case, the '/bin' directory on a Unix-like system)
path = '/bin'

# Get the list of all files and directories in the specified path
dir_list = os.listdir(path)

# Print a message showing the path being listed
print("Files and directories in '", path, "' :")

# Print the list of files and directories
print(dir_list)