'''
Exercises of the book "Think python"
14.12.3 Exercise:
'''

# In a large collection of MP3 files, there may be more than one 
# copy of the same song, stored in different directories or with 
# different file names. The goal of this exercise is to search 
# for duplicates.
# 
# Write a program that searches a directory and all of its subdirectories, 
# recursively, and returns a list of complete paths for all files with a 
# given suffix (like .mp3). Hint: os.path provides several useful 
# functions for manipulating file and path names.
# To recognize duplicates, you can use md5sum to compute a “checksum” 
# for each files. If two files have the same checksum, they probably 
# have the same contents.
# To double-check, you can use the Unix command diff.
# Solution: http://thinkpython2.com/code/find_duplicates.py.

import os
import hashlib


def get_paths(suffix, start_folder, paths = []):
    """Gets all complete paths to all files in directory with a given suffix"""

    # Go through all files in directory
    for name in os.listdir(start_folder):

        # Work only with names with passed suffix
        length_suffix = len(suffix)
        
        # Get an absolute path
        path = os.path.join(start_folder, name)
        # Check type of 'name'
        if os.path.isfile(path):
            # If it's a file
            if name[-length_suffix:] == suffix:
                paths.append(path)
        else:
            # If it's a directory
            get_paths(suffix, path, paths)

    return paths


def find_duplicates(paths_list):
    """Find duplicates of files in list of files"""

    paths_hashsums = {}
    duplicates = []
    # Go through all paths
    for file_path in paths_list:

        # Get MD5 checksum for each file
        hash_sum = md5(file_path)
        if paths_hashsums.get(hash_sum) is not None:
            # If it's duplicate
            duplicates.append(file_path)
        else:
            # If it's not a duplicate
            paths_hashsums[hash_sum] = file_path
    return duplicates


def md5(fpath):
    """Gets an MD5 checksum of a file"""

    hash_md5 = hashlib.md5()
    with open(fpath, "rb") as f:
        # In case file is too big. It needs to be checked through loop
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def process_folder(folder_name, file_type):
    """Processes folder for duplicates with passed type of files"""

    # Get paths to all files
    files_paths = get_paths(file_type, folder_name)
    # get all duplicates
    duplicated_files = find_duplicates(files_paths)
    # Show the user all duplicates
    for i in duplicated_files:
        print(i)


if __name__ == "__main__":
    process_folder("chapter14\\test_folder", ".mp3")
