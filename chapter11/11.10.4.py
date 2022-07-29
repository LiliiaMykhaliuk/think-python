'''
Exercises of the book "Think python"
11.10.4 Exercise:
'''

# If you did Exercise 7, you already have a function named has_duplicates that takes a list as
# a parameter and returns True if there is any object that appears more than once in the list.
# 
# Use a dictionary to write a faster, simpler version of has_duplicates. Solution:
# http://thinkpython2.com/code/has_duplicates.py.

import time

def has_duplicates(list_in):
    """Function checks if there is any duplicated elements in the list"""

    list_dict = {}
    for i in list_in:
        if i in list_dict:
            return True
        list_dict[i] = 1
    return False

# False
print(has_duplicates([1, 2, 3, 4]))
# False
print(has_duplicates(["1", 1, 3, 4]))
# True
print(has_duplicates([2, 1, 1, 4]))

# Exercise 10.15.7 (For test)
def has_duplicates_2(list_in):
    """Function checks if there is any duplicated elements in the list"""

    for i in list_in:
        if list_in.count(i) > 1:
            return True
    return False

test_list = list(range(10000))

# Check time of the first function
start_time = time.time()
has_duplicates(test_list)
print("Has_duplicates with dict: --- %s seconds ---" % (time.time() - start_time))

# Check time of the second function
start_time = time.time()
has_duplicates_2(test_list)
print("Has_duplicates with list: --- %s seconds ---" % (time.time() - start_time))
