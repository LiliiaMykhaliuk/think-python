'''
Exercises of the book "Think python"
11.10.6 Exercise:
'''


# Here’s another Puzzler from Car Talk (http://www.cartalk.com/content/puzzlers):
# 
#     This was sent in by a fellow named Dan O’Leary. He came upon a common one-
#     syllable, five-letter word recently that has the following unique property. When you
#     remove the first letter, the remaining letters form a homophone of the original word,
#     that is a word that sounds exactly the same. Replace the first letter, that is, put it
#     back and remove the second letter and the result is yet another homophone of the original
#     word. And the question is, what’s the word?
#     Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter word,
#     ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first letter, I
#     am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the rack on that
#     buck! It must have been a nine-pointer!’ It’s a perfect homophone. If you put the ‘w’
#     back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is a real
#     word, it’s just not a homophone of the other two words.
# 
#     But there is, however, at least one word that Dan and we know of, which will yield two
#     homophones if you remove either of the first two letters to make two, new four-letter
#     words. The question is, what’s the word?
# 
# 
# You can use the dictionary from Exercise 1 to check whether a string is in the word
# list.
# 
# To check whether two words are homophones, you can use the CMU Pronouncing Dictionary.
# You can download it from http://www.speech.cs.cmu.edu/cgi-bin/cmudict or from
# http://thinkpython2.com/code/c06d and you can also download
# http://thinkpython2.com/code/pronounce.py, which provides a function named
# read_dictionary that reads the pronouncing dictionary and returns a Python dictionary
# that maps from each word to a string that describes its primary pronunciation.
# 
# Write a program that lists all the words that solve the Puzzler. Solution:
# http://thinkpython2.com/code/homophone.py.

import os


def read_dictionary(path):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.
    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".
    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(path)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


def invert_dict(d):
    """Inverts dict and makes pronunciation a key,
       and list of words with the same pronunciation - value.
    """

    inverse_singles = dict()
    inverse_plural = dict()
    for key in d:
        val = d[key]
        if val not in inverse_singles:
            inverse_singles[val] = [key]
        elif 3 < len(key) < 6:
            inverse_plural.setdefault(val, inverse_singles[val])
            inverse_plural[val].append(key)
    return inverse_plural


def find_homophones(words_dict):
    """Finds words that are homophones and print them"""

    # Check each list of words for each pronunciation
    for words in words_dict.values():
        for i in words:

            # Get new words from each 5-letters word
            if len(i) == 5:
                new_word1 = i[1:]
                new_word2 = i[0] + i[2:]

                # Check if they exists
                if new_word1 != new_word2 and new_word1 in words and new_word2 in words:
                    print(f"Word: {i}. Minus first char: {new_word1}. Minus second char: {new_word2}")

# Get a path to the file with pronunciation of words
path = os.path.sep.join(["chapter11", "c06d.txt"])

# Create dict with word as a key and pronunciation as a value
pron_dict = read_dictionary(path)

# Create invert dict with pronunciation as a key
invertDict = invert_dict(pron_dict)

# Find homophones
find_homophones(invertDict)
