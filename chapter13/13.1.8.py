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

import string
import os
import random

def process_book_markov_analysis(PATH):
    """"Processes book by performing Markov analysis"""

    # Get a list of punctuation
    punct = list(string.punctuation)

    # Create a dict for translation with punctuation in UNIcode
    replace_dict = {}
    for c in punct:
        replace_dict.setdefault(ord(c), "")

    # Delete punctuation. Lower case. Split words into list
    markov_analisys = {}

    with open(PATH, 'r') as f:

        # Skipping header
        for line in f:
            if line[:3] == "***":
                break
        f.readline()

        # Left words from the previous line (to make analisys continue where it's ended)
        left_words = []

        # Go through all words
        for line in f:
            # Delete punctuation. Lower case. Split words into list
            line = line.translate(replace_dict).strip().lower()
            words = line.split()

            # Skip empty lines
            if not words:
                continue

            # Process last 3 words from the previous line
            if left_words:
                words = left_words + words

            # Perform Merkov analysis
            for i, word in enumerate(words):

                # Process last 3 words the next line for keeping book together
                if i < len(words) - 3:

                    # Get sufix and prefix
                    prefix = " ".join([word, words[i + 1]])
                    sufix = words[i + 2]

                    # Add prefix and sufix to the list
                    if markov_analisys.get(prefix) is not None:
                        if sufix not in markov_analisys[prefix]:
                            markov_analisys[prefix].append(sufix)
                    else:
                        markov_analisys[prefix] = [sufix]
                else:
                    left_words = words[-3:]
                    break
    return markov_analisys


def generate_random_text(markov_dict, lenght):
    """Generates random text from the dict created by Markov analysis

    marcov_dict: dictionary with (prefix : list of possible sufixes ) pairs
    lenght: the lenght of the generated text
    """

    text = []

    for i in range(lenght):

        # Create empty list of words for the next choice
        generetad_words = []

        # Get the prefix
        if i == 0:
            chosen_prefix = random.choice(list(markov_dict.keys()))
        else:
            chosen_prefix = next_prefix

        # Split the prefix into words
        generetad_words = chosen_prefix.split()

        # Choose random sufix from possible sufixes for current prefix
        chosen_sufix = random.choice(markov_dict[chosen_prefix])

        generetad_words.append(chosen_sufix)

        # Give prefix for the next iteration (second word from the current prefix + sufix)
        next_prefix =" ".join(generetad_words[1:])

        # Append first word of the prefix to the list
        # Prevent duplicates. Append word only if it's not needed anymore for the next sufix
        next_word = generetad_words[0]
        text.append(next_word)

        #Get the text
        get_result = " ".join(text)

    return get_result



# Get a path to the file with text
PATH = os.path.sep.join(["chapter13", "gunetberg.txt"])

result = process_book_markov_analysis(PATH)
print(generate_random_text(result, 50))
