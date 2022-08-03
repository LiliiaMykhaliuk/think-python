'''
Exercises of the book "Think python"
10.15.3 Exercise:
'''
# Write a function called middle that takes a list and returns a new list that contains all but the
# first and last elements. For example:
# 
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]

def middle(list_in):
    """Function returns new list by cutting first and last index from the list """

    return list_in[1:len(list_in) - 1]

print(middle([1, 2, 3]))
print(middle([1, 2, 3, 8, 9]))
print(middle([1, 2]))
