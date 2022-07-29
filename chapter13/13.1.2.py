'''
Exercises of the book "Think python"
13.1.2 Exercise:
'''
# Go to Project Gutenberg (http://gutenberg.org) and download your favorite out-of-
# copyright book in plain text format.
# 
# Modify your program from the previous exercise to read the book you downloaded, skip over
# the header information at the beginning of the file, and process the rest of the words as
# before.
# 
# Then modify the program to count the total number of words in the book, and the number of
# times each word is used.
# 
# Print the number of different words used in the book. Compare different books by different
# authors, written in different eras. Which author uses the most extensive vocabulary?

import os
import string

# Get a list of punctuation
punct = list(string.punctuation)
replace_dict = {}

# Create a dict for translation with UNIcode numbers
for c in punct:
    replace_dict.setdefault(ord(c), "")

# Get a path to the file with text
PATH = os.path.sep.join(["chapter13", "gunetberg.txt"])

# Easy test case (Uncomment)
# path = os.path.sep.join(["chapter13", "test.txt"])

# Delete punctuation. Lower case. Split words into list 
all_words = {}

with open(PATH, 'r') as f:

    # Skipping header
    for line in f:
        if line[:3] == "***":
            break
    f.readline()

    # Go through all words
    for line in f:
        # Delete punctuation. Lower case. Split words into list
        line = line.translate(replace_dict).strip().lower()
        words = line.split()

        # Add unique words to the dict and count their frequency
        for word in words:
            all_words.setdefault(word, 0)
            if all_words.get(word) is not None:
                all_words[word] = all_words[word] + 1

# Number of time each word is used
for key, value in all_words.items():
    print(f"{key} : {value}")

# Total number of words in the book
print("Total amount of words: ", len(all_words))
