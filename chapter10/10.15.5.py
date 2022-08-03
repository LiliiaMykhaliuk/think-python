'''
Exercises of the book "Think python"
10.15.5 Exercise:
'''
# Write a function called is_sorted that takes a list as a parameter and returns
# True if the list is sorted in ascending order and False otherwise. For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False

def is_sorted(list_in):
    """Function checks if list is sorted in ascending order"""

    return list_in == sorted(list_in)

a = [1, 3, 2]

# Unsorted
print(is_sorted(a))

b = [1, 2, 3]
# Sorted
print(is_sorted(b))
