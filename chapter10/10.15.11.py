'''
Exercises of the book "Think python"
10.15.11 Exercise:
'''
# Two words are a “reverse pair” if each is the reverse of the other. Write a program that finds
# all the reverse pairs in the word list. Solution:
# http://thinkpython2.com/code/reverse_pair.py.

import bisect
import os

def reverse_pair(list_in):
    """Function checks list for all reversed pairs"""

    pairs = []
    for list_word in list_in:

        # If the reverse word is the same word -> out
        if list_word == list_word[::-1]:
            continue

        # Check if reverse word is in the list of words
        if in_bisect_cheat(list_in, list_word[::-1]):
            pairs.append([list_word, list_word[::-1]])
    return pairs
    
def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word

# Get the path to the file words.txt
path = os.path.sep.join(["chapter10", "words.txt"])

# Create a list of words from file words.txt
words = []
with open(path, "r") as f:
    for i in f:
        words.append(f.readline().strip())
words.sort()

print(reverse_pair(words))
