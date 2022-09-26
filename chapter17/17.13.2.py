'''
Exercises of the book "Think python"
17.13.2 Exercise:
'''

# This exercise is a cautionary tale about one of the most common, and difficult to find,
# errors in Python. Write a definition for a class named Kangaroo with the following methods:
#
# 1. An __init__ method that initializes an attribute named pouch_contents to an empty list.
# 2. A method named put_in_pouch that takes an object of any type and adds it to pouch_contents.
# 3. A __str__ method that returns a string representation of the Kangaroo object and the
#    contents of the pouch.
#
# Test your code by creating two Kangaroo objects, assigning them to variables named kanga and roo,
# and then adding roo to the contents of kanga’s pouch.
#
# Download http://thinkpython2.com/code/BadKangaroo.py. It contains a solution to the previous problem
# with one big, nasty bug. Find and fix the bug.
#
# If you get stuck, you can download http://thinkpython2.com/code/GoodKangaroo.py, which explains the
# problem and demonstrates a solution.

from __future__ import print_function, division

"""
WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!
"""

class Kangaroo:
    """A Kangaroo is a marsupial."""
   
    def __init__(self, name):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.pouch_contents = []

    def __str__(self):
        """Return a string representation of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)

# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.
