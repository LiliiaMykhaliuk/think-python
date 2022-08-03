'''
Exercises of the book "Think python"
10.15.9 Exercise:
'''
# Write a function that reads the file words.txt and builds a list with one element per word.
# Write two versions of this function, one using the append method and the other using the
# idiom t = t + [x]. Which one takes longer to run? Why?
# 
# Solution: http://thinkpython2.com/code/wordlist.py.

import os
import time

path = os.path.sep.join(["chapter10", "words.txt"])

def list_append():
    """Function appends words to the list with 'append' """

    l_append = []
    with open(path, 'r') as f:
        for i in f:
            l_append.append(f.readline().strip())
    return l_append

def list_idiom():
    """Function appends words to the list with idiom t = t + [x] """

    l_idiom = []
    with open(path, 'r') as f:
        for i in f:
            l_idiom = l_idiom + [f.readline().strip()]
    return l_idiom

# Check time of the first function
start_time = time.time()
list_append()
print("Append: --- %s seconds ---" % (time.time() - start_time))

# Check time of the second function
start_time = time.time()
list_idiom()
print("Idiom: --- %s seconds ---" % (time.time() - start_time))
