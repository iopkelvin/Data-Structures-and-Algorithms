'''
Finding Files
For this problem, the goal is to write code for finding all files under a
directory (and all directories beneath it) that end with '.c'

Python's os module will be useful-in particular, you may want to use the following resources:

Note: os.walk() is a handy Python method which can achieve this task very easily.
        However, for this problem you are not allowed to use os.walk().
'''


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = []
    # Check if path exists
    if (os.path.exists(path)):
        for file in os.listdir(path):
            file_path = path + '/' + file
            # Check if file is a directory
            if os.path.isdir(file_path):
                # Recursion if file is actually a dictionary
                # Also add result to paths
                paths += find_files(suffix, file_path)
            # Not a directory, it is a file
            else:
                # If the file ends with suffix add the filepath to paths
                if file.endswith(suffix):
                    paths.append(file_path)
        return paths
    return "{} doesn't exists".format(path)


## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python
import os
# Get current path
path = os.path.abspath(os.getcwd())
# Move to testdir folder
# os.chdir(path + '/testdir')
# Let us print the files in the directory in which you are running this script
print(os.listdir(path + '/testdir'))
# Let us check if this file is indeed a file!
print('Is there a ex.py file?: ', os.path.isfile("./ex.py"))
# Does the file end with .py?
print('does exp.py end with .py?: {}'.format("./ex.py".endswith(".py")))
#####
#####
# Get path of testdir folder
folder_path = './testdir'

# Default test
print("Test 1")
print('Files ending with .c')
print(find_files('.c', folder_path))  # Files ending in .c

# Prints every file
print("\nTest 2")
print('All files in path')
print(find_files('', folder_path))    # All files

# Non existent extension
print("\nTest 3")
print('All files ending with .b')
print(find_files('.b', folder_path))  # Files ending in .b

# Non existent directory
print("\nTest 4")
print('All files ending with .c in nanodegree directory')
print(find_files('.c', './nanodegree'))   # False directory

# Empty Directory
print("\nTest 5")
print('All files ending with .c in emptydir directory')
print(find_files('.c', folder_path+'/emptydir'))   # Empty directory