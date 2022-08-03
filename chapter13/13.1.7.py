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
    """"Processes book into histogram of words frequency"""

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


def get_word_list(freq_dict):
    """Creates a list of unique words"""

    return sorted(freq_dict, key=freq_dict.get, reverse=False)


def get_cumulative_sum(freq_dict):
    """Creates a list with cumulative sum of frequencies of the words"""

    result = []

    # Go through dictionary sorted by word
    for i in sorted(freq_dict, key=freq_dict.get, reverse=False):

        # Make cumulative sum

        if not result:
            # Set first sum
            result.append(freq_dict[i])
            # Save current sum for the next iteration
            last_sum = freq_dict[i]
        else:
            # Create next cumulative sum
            current_sum = freq_dict[i] + last_sum
            # Save current sum for the next iteration
            last_sum = current_sum

            # Save current cumulative sum into list
            result.append(current_sum)

    return result


def bisect_search(given_list, number):
    """Finds index in a list using bisection search.
    Precondition: the words in the list are sorted
    given_list: list of cumulative sum
    word: int
    """

    i = bisect.bisect_left(given_list, number)
    if i == len(given_list):
        return False

    return i


def get_random_word(sum_list, word_list):
    """Chooses random word from the list of unique words

    sum_list: list of cumulative sum of frequencies
    word_list: List of unique words in the book
    """


    # Choose random number
    random_number = random.randrange(0, sum_list[-1])

    # Get the index of the random number in cumulative sum list of frequencies
    index = bisect_search(cumulative_sum, random_number)

    # Get the random word
    random_word = word_list[index]
    
    return random_word


# Get a path to the file with text
PATH = os.path.sep.join(["chapter13", "gunetberg.txt"])

# Process book into histogram of word frequency
word_frequency = process_book(PATH)

# Get list of unique words from histogram
unique_words = get_word_list(word_frequency)

# Create list of cumulative sum of frequencies from histogram
cumulative_sum = get_cumulative_sum(word_frequency)

# Get the random word
result = get_random_word(cumulative_sum, unique_words)
print(result)
