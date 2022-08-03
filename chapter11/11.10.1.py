'''
Exercises of the book "Think python"
11.10.1 Exercise:
'''
# Write a function that reads the words in words.txt and stores them as keys in a dictionary. It
# doesn’t matter what the values are. Then you can use the in operator as a fast way to check
# whether a string is in the dictionary.
# 
# If you did Exercise 10, you can compare the speed of this implementation with the list in
# operator and the bisection search.

import os
import bisect
import time

path = os.path.sep.join(["chapter10", "words.txt"])

words = {}

def make_dict():
    """Function create a dict from words in file word.txt"""

    with open(path, "r") as f:
        for i in f:
            words.update({f.readline().strip() : ""})

# Function for comparison with list creation
l_append = []

def list_append():
    """Function appends words to the list with 'append' """

    with open(path, 'r') as f:
        for i in f:
            l_append.append(f.readline().strip())

# Function for comparison hash search with bisection search
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
# Test
# Check time of the list function
start_time = time.time()
list_append()
print("List: --- %s seconds ---" % (time.time() - start_time))

# Check time of the dict function
start_time = time.time()
make_dict()
print("Dict: --- %s seconds ---" % (time.time() - start_time))

# Check time of the list bisection search
start_time = time.time()
if in_bisect_cheat(l_append, "yogurt"):
    print("   yogurt is in list")
print("List in: --- %s seconds ---" % (time.time() - start_time))

# Check time of the dict in function
start_time = time.time()
if "yogurt" in words:
    print("   yogurt is in dict")
print("Dict in: --- %s seconds ---" % (time.time() - start_time))
