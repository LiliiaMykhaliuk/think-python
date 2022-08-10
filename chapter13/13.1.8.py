'''
Exercises of the book "Think python"
13.1.8 Exercise:
'''

# Markov analysis:
# 
#  1. Write a program to read a text from a file and perform Markov analysis. The result 
#     should be a dictionary that maps from prefixes to a collection of possible suffixes. 
#     The collection might be a list, tuple, or dictionary; it is up to you to make an
#     appropriate choice. You can test your program with prefix length two, but you 
#     should write the program in a way that makes it easy to try other lengths.
#  2. Add a function to the previous program to generate random text based on the Markov 
#     analysis. Here is an example from Emma with prefix length 2:
#     He was very clever, be it sweetness or be angry, ashamed or only amused, at such a 
#     stroke. She had never thought of Hannah till you were never meant for me?" "I 
#     cannot make speeches, Emma:" he soon cut it all himself.
#     For this example, I left the punctuation attached to the words. The result is 
#     almost syntactically correct, but not quite. Semantically, it almost makes 
#     sense, but not quite.
# 
#     What happens if you increase the prefix length? Does the random text make 
#     more sense?
# 
#  3. Once your program is working, you might want to try a mash-up: if you combine 
#     text from two or more books, the random text you generate will blend the 
#     vocabulary and phrases from the sources in interesting ways.
#     Credit: This case study is based on an example from Kernighan and 
#     Pike, The Practice of Programming, Addison-Wesley, 1999.
# 
# You should attempt this exercise before you go on; then you can 
# download my solution from http://thinkpython2.com/code/markov.py. 
# You will also need http://thinkpython2.com/code/emma.txt.

import os
import random

def process_line(text):
    """Deletes whitespaces. Lower case of words. Split text into list"""

    # Delete whitespaces. Lower case.
    new_text = text.strip().lower()
    # Split words into list
    processed_text = new_text.split()

    return processed_text


def get_all_words_in_book(PATH):
    """"Processes book and makes list of all words from the book"""

    words_in_book = []

    with open(PATH, 'r') as f:

        # Skip header
        for line in f:
            if line[:3] == "***":
                break
        f.readline()

        # Go through the book line by line
        for line in f:

            # Skip empty lines
            if not line:
                continue

            # Delete punctuation, whitespaces, make case of words lower, split line into list of words
            words = process_line(line)

            # Make list of words from the book
            words_in_book.extend(words)

    return words_in_book


def perform_markov_analysis(words_list):
    """Performs Markov analysis with given words"""

    markov_dict = {}

    # Perform Markov analysis
    for i, word in enumerate(words_list):

        # Last 2 words can't be a prefix
        if i > len(words_list) - 3:
            break

        # Get prefix (2 words)
        prefix = " ".join([word, words_list[i + 1]])

        # Get suffix (next word after prefix)
        suffix = words_list[i + 2]

        # Add prefix and suffix to the dict
        markov_dict.setdefault(prefix, [suffix])

        if suffix not in markov_dict[prefix]:
            markov_dict[prefix].append(suffix)

    return markov_dict


def generate_random_text(markov_dict, length):
    """Generates random text from the dict created by Markov analysis

    markov_dict: dictionary with [prefix : list of possible suffixes] pairs
    length: the length of the generated text
    """

    generated_text = []

    # Generate words for the text
    for i in range(length):

        # Create empty list of words for the next choice
        generated_words = []

        # Get prefix
        if i == 0:
            # Get random prefix as a first prefix
            chosen_prefix = random.choice(list(markov_dict.keys()))
        else:
            # Get prefix created on the last iteration
            chosen_prefix = next_prefix

        # Choose random suffix from all possible suffixes for current prefix
        chosen_suffix = random.choice(markov_dict[chosen_prefix])

        # Make a list of generated words in current iteration
        generated_words = chosen_prefix.split()
        generated_words.append(chosen_suffix)

        # Make a prefix for the next iteration
        next_prefix = " ".join(generated_words[1:])

        # Append word to the generated text
        generated_text.append(generated_words[0])

    #Get the text
    result = " ".join(generated_text)

    return result


def process_book(PATH):
    """Processes book by performing Markov analysis"""

    # Make words list from the book
    all_words = get_all_words_in_book(PATH)

    # Do Markov analysis
    markov_analysis_result = perform_markov_analysis(all_words)

    return markov_analysis_result


# Get a path to the file with text
PATH = os.path.sep.join(["chapter13", "gunetberg.txt"])

# Process book with Markov analysis
ANALYSIS_RESULT = process_book(PATH)

# Generate text with certain length from analysis result
TEXT = generate_random_text(ANALYSIS_RESULT, 50)

print(TEXT)
