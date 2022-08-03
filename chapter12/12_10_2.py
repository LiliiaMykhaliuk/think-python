'''
Exercises of the book "Think python"
12.10.2 Exercises:
'''
# More anagrams!
# 
# Write a program that reads a word list from a file (see Section 9.1) and prints all the
# sets of words that are anagrams.
# Here is an example of what the output might look like:
# 
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']
# Hint: you might want to build a dictionary that maps from a collection of letters to a
# list of words that can be spelled with those letters. The question is, how can you
# represent the collection of letters in a way that can be used as a key?
# 
# Modify the previous program so that it prints the longest list of anagrams first,
# followed by the second longest, and so on.
# In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter
# on the board, to form an eight-letter word. What collection of 8 letters forms the most
# possible bingos?
# Solution: http://thinkpython2.com/code/anagram_sets.py.

import os

PATH = os.path.sep.join(['chapter12', 'words.txt'])

def find_anagrams(PATH):
    """The function find all anagrams (words with the same letters)"""

    with open(PATH, 'r') as f:

        words = {}
        anagrams = {}
        for i in f:

            # Cut \n from the word
            word = i.strip()

            # Sort letters in a tuple
            key = tuple(sorted(word))

            # Add anagram word If word with same letters already exists
            if words.get(key) is not None:
                val = words.get(key)

                # Add word-anagram if it's not in the list
                if key not in anagrams:
                    anagrams[key] = [val]
                else:
                    if val not in anagrams.get(key):
                        anagrams.get(key).append(val)

                # Add current word
                anagrams.get(key).append(word)

            else:
                words[key] = word

        return anagrams

anagrams_list = find_anagrams(PATH)

# Print anagrams in decreasing order
for j in sorted(anagrams_list, key=lambda k: len(anagrams_list[k]), reverse = True):
    print(anagrams_list[j])
