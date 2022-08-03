'''
Exercises of the book "Think python"
10.15.4 Exercise:
'''
# Write a function called chop that takes a list, modifies it by removing the first and last
# elements, and returns None. For example:
# 
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]

def chop(list_in):
    """Function cuts first and last index of the list"""
    
    del list_in[0]
    del list_in[-1]

a = [1, 2, 3, 4]

# Show that function returns None
print(chop(a))

# Show that list changed
print(a)
