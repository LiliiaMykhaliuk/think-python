'''
Exercises of the book "Think python"
13.1.5 Exercise:
'''

# Write a function named choose_from_hist that takes a histogram as defined in Section 11.2
# and returns a random value from the histogram, chosen with probability in proportion to
# frequency. For example, for this histogram:

import random

def histogram(word):
    """Makes a histogram of frequency of the letters in the word"""

    frequency = {}
    for letter in word:
        frequency.setdefault(letter, word.count(letter))

    return frequency

def choose_from_hist(hist, initial_word):
    """Counts probability to be chosen of a random char in a proportion to frequency"""

    # Get a random letter
    keys_list = list(hist.keys())
    random_letter = random.choice(keys_list)

    # Count probabiblity
    probability = round(hist[random_letter] / len(initial_word), 2)

    return f"{random_letter} has probability: {probability}"


USER_INPUT = input("Enter any word: ")

WORD_HIST = histogram(USER_INPUT)
print(choose_from_hist(WORD_HIST, USER_INPUT))
