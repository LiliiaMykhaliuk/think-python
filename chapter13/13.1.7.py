'''
Exercises of the book "Think python"
13.1.7 Exercise:
'''

# An alternative is:
# 
# 1. Use keys to get a list of the words in the book.
# 2. Build a list that contains the cumulative sum of the word frequencies (see Exercise 2).
#    The last item in this list is the total number of words in the book, n.
# 3. Choose a random number from 1 to n. Use a bisection search (See Exercise 10) to find
#    the index where the random number would be inserted in the cumulative sum.
# 4. Use the index to find the corresponding word in the word list.
# 
# Write a program that uses this algorithm to choose a random word from the book.
# Solution: http://thinkpython2.com/code/analyze_book3.py.

import os
import string
import bisect
import random

def process_book(PATH):
    """"Processes book into word list"""

    # Get a list of punctuation
    punct = list(string.punctuation)

    # Create a dict for translation with punctuation in UNIcode
    replace_dict = {}
    for c in punct:
        replace_dict.setdefault(ord(c), "")

    # Delete punctuation. Lower case. Split words into list
    all_words = {}

    with open(PATH, 'r') as f:

        # Skipping header
        for line in f:
            if line[:3] == "***":
                break
        f.readline()

        # Go through all words
        for line in f:
            # Delete punctuation. Lower case. Split words into list
            line = line.translate(replace_dict).strip().lower()
            words = line.split()

            # Add unique words to the dict and count their frequency
            for word in words:
                all_words.setdefault(word, 0)
                if all_words.get(word) is not None:
                    all_words[word] = all_words[word] + 1
    return all_words

# Get a path to the file with text
PATH = os.path.sep.join(["chapter13", "gunetberg.txt"])

word_frequency = process_book(PATH)

def get_word_list(freq_dict):
    """Creates a list of unique words"""

    return sorted(freq_dict, key=freq_dict.get, reverse=False)

def get_cumulative_sum(freq_dict):
    """Creates a list with cumulative summ of frequences of the words"""

    result = []
    # Go through sorted by word dictionary
    for i in sorted(freq_dict, key=freq_dict.get, reverse=False):

        # Set first summ
        if not result:
            result.append(freq_dict[i])
            # Save current summ for the next iteration
            last_sum = freq_dict[i]
        
        # Create next cummulative summ
        current_sum = freq_dict[i] + last_sum
        # Save current summ for the next iteration
        last_sum = current_sum

        # Save next cummulative summ
        result.append(current_sum)
    return result

def in_bisect_cheat(given_list, number):
    """Finds index in a list using bisection search.
    Precondition: the words in the list are sorted
    given_list: list of cumulative cums
    word: int
    """
    i = bisect.bisect_left(given_list, number)
    if i == len(given_list):
        return False

    return i

# Create list of unique words
unique_words = get_word_list(word_frequency)

# Create list of cumulative sum
cummulative_sum = get_cumulative_sum(word_frequency)

# Choose random number
random_number = random.randrange(0, cummulative_sum[-1])

# Get the index of the word in cumulative sum
word_index = in_bisect_cheat(cummulative_sum, random_number)

# In case random choice will choose the last word
if word_index > len(unique_words) - 1:
    word_index -= 1

# Get the random word
print(unique_words[word_index])
