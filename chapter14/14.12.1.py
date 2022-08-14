'''
Exercises of the book "Think python"
14.12.1 Exercise:
'''

# Write a function called sed that takes as arguments a pattern string, 
# a replacement string, and two filenames; it should read the first 
# file and write the contents into the second file (creating it if necessary). 
# If the pattern string appears anywhere in the file, it should be 
# replaced with the replacement string.
# 
# If an error occurs while opening, reading, writing or closing 
# files, your program should catch the exception, print an error 
# message, and exit. 
# Solution: http://thinkpython2.com/code/sed.py.

import os

def move_text_with_replacement(pattern_str, replacement_str, read_f, write_f):
    "Copies text into another file and replaces pattern string with replacement"

    # Create path to the read file
    read_path = os.path.sep.join(["chapter14", read_f])

    # Read file
    try:
        with open(read_path, 'r') as read_file:
            text = read_file.read()
    except:
        print("Problems with reading the file")

    # Replace string
    text = text.replace(pattern_str, replacement_str)

    # Create path to the file to write
    write_path = os.path.sep.join(["chapter14", write_f])

    # Write text into another file
    try:
        with open(write_path, 'w') as write_file:
            write_file.write(text)
    except:
        print("Problems with writing into file")

move_text_with_replacement("On insensible possession", "In the beautiful house", "random_text.txt", "random_text_new.txt")
