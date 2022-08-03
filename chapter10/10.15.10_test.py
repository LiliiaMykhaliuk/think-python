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

def in_bisect(input, target):
    """Function search for the target in the list of words by using bisecting search"""
    
    # Get first middle of the list
    lenght = len(input)
    middle = lenght // 2

    last_middle = -1

    # Array of indexes that we currently looking at
    start = 0
    end = lenght

    while last_middle != middle:
        last_middle = middle

        # Check if we got our target
        if input[middle] == target:
            return middle

        # Search in the first half
        if target < input[middle]:
            end = middle

            # Calculate step
            step = (end - start) // 2
            if step == 0:
                step = 1
            # Step back
            middle -= step

        # Search in the second half
        elif target > input[middle]:
            start = middle

            # Calculate step
            step = ((end - start) // 2)
            if step == 0:
                step = 1
            # Step forward
            middle += step

        if last_middle == middle:
            break
    return False

# My test cases
# print("My list. Works fine (not gound) - >", in_bisect(["aaa", "bbb", "ccc", "dddd", "eeeet"], "eeee"))
# print("My list. Works fine (found) - > ", in_bisect(["aaa", "bbb", "ccc", "dddd", "eeee"], "eeee"))


# Test1
test_words = ['zananas', 'zanders', 'zanies', 'zanily', 'zaninesses']
print("Test1. Index of the target word ->",in_bisect(test_words, 'zanies'))

# Test2
test_words = [0, 1]
print("Test2. Index of the target word ->", in_bisect(test_words, 0))

# Create a list of words from file words.txt
path = os.path.sep.join(["chapter10", "words.txt"])

words = []
with open(path, "r") as f:
    for i in f:
        words.append(i.strip())
words.sort()
#print(words)

# Test3. Words from words.txt
print("Test3. Words from words.txt. Index of the target word ->", in_bisect(words, "zymurgy" ))
# Test4. Words from words.txt
print("Test4. Words from words.txt. Index of the target word ->", in_bisect(words, "aalii" ))
