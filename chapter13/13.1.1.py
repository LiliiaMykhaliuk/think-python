'''
Exercises of the book "Think python"
13.1.1 Exercise:
'''

# Write a program that reads a file, breaks each line into words, strips whitespace
# and punctuation from the words, and converts them to lowercase.
# 
# Hint: The string module provides a string named whitespace, which contains space,
# tab, newline, etc., and punctuation which contains the punctuation characters.
# Let’s see if we can make Python swear:
# 
# >>> import string
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# Also, you might consider using the string methods strip, replace
# and translate.

import os
import string

# Get a list of punctuation
punct = list(string.punctuation)
replace_dict = {}

# Create a dict for translation with UNIcode numbers
for c in punct:
    replace_dict.setdefault(ord(c), "")

# Get a path to the file with text
path = os.path.sep.join(["chapter13", "text_1_1.txt"])

# Delete punctuation. Lower case. Split words into list 
words = []
with open(path, 'r') as f:
    for line in f:
        line = line.translate(replace_dict).strip().lower()
        words += line.split()
print(words)
