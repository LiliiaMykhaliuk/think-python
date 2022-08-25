'''
Exercises of the book "Think python"
14.12.2 Exercise:
'''

# If you download my solution to Exercise 2 from 
# http://thinkpython2.com/code/anagram_sets.py, you’ll see that it 
# creates a dictionary that maps from a sorted string of letters 
# to the list of words that can be spelled with those letters. 
# For example, 'opst' maps to 
# the list ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
# 
# Write a module that imports anagram_sets and provides two new 
# functions: store_anagrams should store the anagram dictionary 
# in a “shelf”; read_anagrams should look up a word and return 
# a list of its anagrams. 
# Solution: http://thinkpython2.com/code/anagram_db.py.

import shelve
import os
from anagrams import all_anagrams


def store_anagrams(anagrams_dict):
    """Stores anagrams in a shelf"""

    # Store the anagrams dict in 'shelf'
    with shelve.open('saved_anagrams') as db:
        db['anagrams_dict'] = anagrams_dict


def read_anagrams(word):
    """Looks for the list of anagrams for the word"""

    # Read anagrams dictionary
    with shelve.open('saved_anagrams') as db:
        saved_anagrams = db.get('anagrams_dict')

    # Get the list of anagrams for the word
    key = ''.join(sorted(word))
    anagrams_list = saved_anagrams.get(key, "No such word in the dict")
    anagrams_list.remove(word)

    return anagrams_list


# Test program
if __name__ == "__main__":
    path = os.path.sep.join(["chapter14", "words.txt"])

    anagrams = all_anagrams(path)
    store_anagrams(anagrams)
    result = read_anagrams("pots")

    print(result)
