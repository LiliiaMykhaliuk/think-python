'''
Exercises of the book "Think python"
13.1.9 Exercise:
'''
# The “rank” of a word is its position in a list of words sorted by frequency: the most common 
# word has rank 1, the second most common has rank 2, etc.
# 
# Zipf’s law describes a relationship between the ranks and frequencies of words in natural 
# languages (http://en.wikipedia.org/wiki/Zipf's_law). Specifically, it predicts that the 
# frequency, f, of the word with rank r is:
# 
#                       f = c r−s 
# where s and c are parameters that depend on the language and the text. If you take the 
# logarithm of both sides of this equation, you get:
# 
#                   logf = logc − s logr 
# So if you plot log f versus log r, you should get a straight line with slope −s and 
# intercept log c.
# 
# Write a program that reads a text from a file, counts word frequencies, and prints 
# one line for each word, in descending order of frequency, with log f and log r. 
# Use the graphing program of your choice to plot the results and check whether 
# they form a straight line. Can you estimate the value of s?
# 
# Solution: http://thinkpython2.com/code/zipf.py. To run my solution, 
# you need the plotting module matplotlib. If you installed Anaconda, you 
# already have matplotlib; otherwise you might have to install it.

# Get a path to the file with text

import os

get
PATH = os.path.sep.join(["chapter13", "13_1_9_text.txt"])
