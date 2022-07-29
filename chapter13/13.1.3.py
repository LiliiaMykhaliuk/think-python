'''
Exercises of the book "Think python"
13.1.3 Exercise:
'''

# Modify the program from the previous exercise to print the 20 most frequently used words in
# the book.

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

# Easy test case (Uncomment)
#PATH = os.path.sep.join(["chapter13", "test.txt"])

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

# Set counter for 20 words
counter = 0

# Go through sorted by value dictionary
for k in sorted(all_words, key=all_words.get, reverse=True):
    print(f"{k} : {all_words[k]}")

    # Print only 20 most frequent words
    counter += 1
    if counter > 20:
        break

print("Total amount of words: ", len(all_words))
