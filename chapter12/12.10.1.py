'''
Exercises of the book "Think python"
12.10.1 Exercises:
'''

# Write a function called most_frequent that takes a string and prints the letters in decreasing
# order of frequency. Find text samples from several different languages and see how letter
# frequency varies between languages. Compare your results with the tables at
# http://en.wikipedia.org/wiki/Letter_frequencies. Solution:
# http://thinkpython2.com/code/most_frequent.py.

def most_frequent(phrase):
    """The function count frequency of letters in phrase"""

    # Split phrase to letters
    phrase_in_letters = list(''.join(phrase.split()).lower())

    letters_frequency = {}
    # Count frequency of each letter
    for letter in phrase_in_letters:
        letters_frequency.setdefault(letter, round(((phrase_in_letters.count(letter) * 100) / len(phrase_in_letters)), 2))

    # Print letters in decreasing order of frequency
    for lett in sorted(letters_frequency, key = letters_frequency.get, reverse = True):
        print(f'{lett} : {letters_frequency[lett]} %')

# most_frequent("aaa b c a o")
most_frequent("Let the cat out of the bag")
