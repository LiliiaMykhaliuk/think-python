'''
Exercises of the book "Think python"
10.15.1 Exercise:
'''
# Write a function called nested_sum that takes a list of lists of integers and adds up the
# elements from all of the nested lists. For example:
# 
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21

def nested_sum(in_list):
    """Functions returns the sum of all integers in the list (including nested)"""
    # Make the list of summs of nested lists
    not_nested = list(map(sum, in_list))
    return sum(not_nested)

print(nested_sum([[1, 2, 3], [1, 1, 1], [1,]]))
