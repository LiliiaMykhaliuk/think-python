'''
Exercises of the book "Think python"
11.10.2 Exercise:
'''

# Read the documentation of the dictionary method setdefault and use it to write a more
# concise version of invert_dict. Solution: http://thinkpython2.com/code/invert_dict.py.

def invert_dict(d):
    """The function inverts dictionary"""

    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

print(invert_dict({'a': 3, 'b': 3, 'c': 2}))
