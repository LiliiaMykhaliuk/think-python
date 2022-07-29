'''
Exercises of the book "Think python"
13.1.6 Exercise:
'''
# Python provides a data structure called set that provides many common set operations. You
# can read about them in Section 19.5, or read the documentation at
# http://docs.python.org/3/library/stdtypes.html#types-set.
# 
# Write a program that uses set subtraction to find words in the book that are not in the word
# list. Solution: http://thinkpython2.com/code/analyze_book2.py.

import os
import string

# Get a list of punctuation
punct = list(string.punctuation)

# Create a dict for translation with punctuation in UNIcode
replace_dict = {}
for c in punct:
    replace_dict.setdefault(ord(c), "")

# Get a path to the file with text
PATH = os.path.sep.join(["chapter13", "gunetberg.txt"])

# Delete punctuation. Lower case. Split words into list
all_words = set()

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

        # Add unique words to the set
        for word in words:
            all_words.add(word)

# Get the pass to the word list
PATH2 = os.path.sep.join(["chapter13", "words.txt"])

# Create dict of real words from word_list
word_set = set()
with open(PATH2, 'r') as f2:
    for i in f2:
        word_set.add(i.strip().lower())

def find_not_words(set1, set2):
    """Finds all words from the book that are not in the word list"""

    return set1.difference(set2)

print(find_not_words(all_words, word_set))
