'''
Exercises of the book "Think python"
10.15.10 Exercise:
'''
# To check whether a word is in the word list, you could use the in operator, but it would be
# slow because it searches through the words in order.
# 
# Because the words are in alphabetical order, we can speed things up with a bisection search
# (also known as binary search), which is similar to what you do when you look a word up in
# the dictionary (the book, not the data structure). You start in the middle and check to see
# whether the word you are looking for comes before the word in the middle of the list. If so,
# you search the first half of the list the same way. Otherwise you search the second half.
# 
# Either way, you cut the remaining search space in half. If the word list has 113,809 words, it
# will take about 17 steps to find the word or conclude that it’s not there.
# 
# Write a function called in_bisect that takes a sorted list and a target value and returns True
# if the word is in the list and False if it’s not.
# 
# Or you could read the documentation of the bisect module and use that! Solution:
# http://thinkpython2.com/code/inlist.py.

import os

def in_bisect(list_in, target):
    """Function search for the target in the list of words by using bisecting search"""

    if list_in == []:
        return False

    middle = len(list_in) // 2

    if list_in[middle] == target:
        return True
    # Search in the first half
    if target < list_in[middle]:
        return in_bisect(list_in[:middle], target)

    # Search in the second half
    if target > list_in[middle]:
        middle += 1
        return in_bisect(list_in[middle:], target)


path = os.path.sep.join(["chapter10", "words.txt"])

# Create a list of words from file words.txt
words = []
with open(path, "r") as f:
    for i in f:
        words.append(f.readline().strip())
words.sort()
print(in_bisect(words, "zymurgies"))

