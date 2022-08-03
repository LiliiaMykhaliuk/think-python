'''
Exercises of the book "Think python"
10.15.7 Exercise:
'''
# Write a function called has_duplicates that takes a list and returns True if there is any
# element that appears more than once. It should not modify the original list.

def has_duplicates(list_in):
    """Function checks if there is any diplicated elements in the list"""

    for i in list_in:
        if list_in.count(i) > 1:
            return True
    return False

# False
print(has_duplicates([1, 2, 3, 4]))
# False
print(has_duplicates(["1", 1, 3, 4]))
# True
print(has_duplicates([2, 1, 1, 4]))
