'''
Exercises of the book "Think python"
12.10.3 Exercises:
'''
# Two words form a “metathesis pair” if you can transform one into the other by swapping two
# letters; for example, “converse” and “conserve”. Write a program that finds all of the
# metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all
# possible swaps. Solution: http://thinkpython2.com/code/metathesis.py. Credit: This
# exercise is inspired by an example at http://puzzlers.org.

# from chapter12.12_10_2.py import find_anagrams - why it doesn't work?

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

def check_letters(word1, word2):
    """The function checks how many letters are different in two words"""

    count = 0
    for let1, let2 in zip(word1, word2):
        if let1 != let2:
            count += 1
        if count > 2:
            return False
    return True

def metathesis_pair(path):
    """The function finds all words that can be transformed one into the other by swapping two letters"""

    possible_pairs = find_anagrams(path)

    # go through each list of anagrams
    for words in possible_pairs.values():

        # Compare words with each other
        for word in words:

            # Go through all list of words with bigger indexes (prevent cheking same pairs)
            step = 1
            while True:

                # Get next word to compare
                index2 = words.index(word) + step
                if index2 > len(words) - 1:
                    break

                # Check if words are metathesis pair
                word2 = words[index2]
                if check_letters(word, word2):
                    print(word, word2)
            
                step +=1

metathesis_pair(PATH)
