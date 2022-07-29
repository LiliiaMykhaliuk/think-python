'''
Exercises of the book "Think python"
13.1.4 Exercise:
'''

# Modify the previous program to read a word list (see Section 9.1) and then print all the words
# in the book that are not in the word list. How many of them are typos? How many of them are
# common words that should be in the word list, and how many of them are really obscure?

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

# Get the pass to the word list
PATH2 = os.path.sep.join(["chapter13", "words.txt"])

# Create dict of real words from word_list
word_dict = {}
with open(PATH2, 'r') as f2:
    for i in f2:
        word_dict[i.strip().lower()] = ""

# Find all words from the book that are not in the word list
not_words = {}
for word, frequency in all_words.items():
    if word_dict.get(word) is None:
        not_words[word] = frequency

# Print words with frequency more than 1. These are possible real words.
counter = 0
for k in sorted(not_words, key=all_words.get, reverse=True):
    if not_words[k] < 2:
        break
    print(f"{k} : {not_words[k]}")
