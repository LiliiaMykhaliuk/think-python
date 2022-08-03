'''
Exercises of the book "Think python"
10.15.12 Exercise:
'''
# Two words “interlock” if taking alternating letters from each forms a new word. For
# example, “shoe” and “cold” interlock to form “schooled”. Solution:
# http://thinkpython2.com/code/interlock.py. Credit: This exercise is inspired by an
# example at http://puzzlers.org.
# 
# 1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all
# pairs!
# 2. Can you find any words that are three-way interlocked; that is, every third letter forms
# a word, starting from the first, second or third?

import bisect
import os

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

def interlock(words):
    """Checks for words that 'interlock'"""

    interlocks = {}
    for word in words:
        # Create possible words from the word
        word1 = word[::2]
        word2 = word[1::2]

        # Check if the each of words exists in the list of words
        if len(word1) == len(word2):
            if in_bisect_cheat(words, word1) and in_bisect_cheat(words, word2):
                interlocks[word] = [word1, word2]
  
    for key, value in interlocks.items():
        print(f"{key} : {value}")

# Get the path to the file words.txt
path = os.path.sep.join(["chapter10", "words.txt"])

# Create a list of words from file words.txt
words = []
with open(path, "r") as f:
    for i in f:
        words.append(i.strip())
words.sort()

interlock(words)
