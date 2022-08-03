'''
Exercises of the book "Think python"
10.15.6 Exercise:
'''
# Two words are anagrams if you can rearrange the letters from one to spell the other. Write a
# function called is_anagram that takes two strings and returns True if they are anagrams.

def is_angram(word1, word2):
    """Function checks if words are anagrams"""

    # False if words have not the same lenght
    if len(word1) != len(word2):
        return False

    # Make list of letters from each word
    letters_word1 = sorted(word1)
    letters_word2 = sorted(word2)

    # Compare them
    if letters_word1 != letters_word2:
        return False
    return True

# True
print(is_angram("noon", "onon"))
# False 
print(is_angram("noon", "onont"))
# False
print(is_angram("noon", "ooon"))
