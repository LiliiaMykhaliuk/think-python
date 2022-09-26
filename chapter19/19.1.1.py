'''
Exercises of the book "Think python"
19.11.1 Exercise:
'''

# The following is a function that computes the binomial coefficient recursively.
# 
# def binomial_coeff(n, k):
#     """Compute the binomial coefficient "n choose k".
# 
#     n: number of trials
#     k: number of successes
# 
#     returns: int
#     """
#     if k == 0:
#         return 1
#     if n == 0:
#         return 0
# 
#     res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
#     return res
# Rewrite the body of the function using nested conditional expressions.
# 
# One note: this function is not very efficient because it ends up computing the same values over and over.
# You could make it more efficient by memoizing (see Section 11.6). But you will find that it’s harder to 
# memoize if you write it using conditional expressions.

import unittest

# Function from the book
def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes

    returns: int
    """
    if k == 0:
        return 1
    if n == 0:
        return 0

    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res

print(binomial_coeff(3, 2))


# My function
def binomial_coeff_my(n, k):
    """Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes

    returns: int
    """

    return 1 if k == 0 else 0 if n == 0 else binomial_coeff_my(n-1, k) + binomial_coeff_my(n-1, k-1)

print(binomial_coeff_my(3, 2))


class Test_Poker_classification(unittest.TestCase):

    def test_my_function(self):

        self.assertEqual(binomial_coeff(3, 2), binomial_coeff_my(3, 2) )

if __name__ == '__main__':
    unittest.main(verbosity=2)
