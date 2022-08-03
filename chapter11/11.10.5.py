'''
Exercises of the book "Think python"
11.10.5 Exercise:
'''

# Two words are “rotate pairs” if you can rotate one of them and get the other (see
# rotate_word in Exercise 5).
# 
# Write a program that reads a wordlist and finds all the rotate pairs. Solution:
# http://thinkpython2.com/code/rotate_pairs.py.

def rotate_word(word, number):
    """Rotates word by using Ceasar cypher"""

        # Create rotate word
    new_word = ""
    for letter in word:
        new_number = ord(letter) + number

        # Incase of zigzag
        if new_number > 122:
            new_number = 96 + (new_number - 122)
        if new_number < 97:
            new_number = 123 + number

        new_word += chr(new_number)
    return new_word

def rotate_pairs(word_list, number):
    """Function rotates word by using Caesar cypher"""
    word_dict = {}
    pairs = {}

    # Convert list into dict
    for word in word_list:
        word_dict.setdefault(word, "")

    for word1 in word_dict:

        # Create rotate word
        new_word = rotate_word(word1, number)

        # Check if there is rotate pair 
        rotated_word = word_dict.get(new_word)
        if rotated_word is not None:
            pairs[word1] = new_word
    return pairs

# Test
print("Test:")
print(rotate_pairs(['cheer', 'dfsgsf', 'sdsdf', 'jolly'], 7))

# Test of zigzag
print("Test of zigzag:")
print(rotate_pairs(['aaaa', 'zzzz', 'yyy', 'jjjj'], -1))
