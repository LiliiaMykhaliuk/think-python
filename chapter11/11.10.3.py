'''
Exercises of the book "Think python"
11.10.3 Exercise:
'''

# Memoize the Ackermann function from Exercise 2 and see if memoization makes
# it possible to evaluate the function with bigger arguments. Hint: no. Solution:
# http://thinkpython2.com/code/ackermann_memo.py.

# def ack(m = 0, n = 0):
#     """Function evaluates the Ackermann function."""
#     
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return ack(m - 1, 1)
#     else:
#         return ack(m - 1, ack(m, n - 1))
memo = {}
def ack(m = 0, n = 0):
    """Function evaluates the Ackermann function."""

    # Try to get memorized return
    val = memo.get(str(m) + str(n), None)
    if val is not None:
        return val

    # If return is not memorized yet
    if m == 0:
        val = n + 1
    elif m > 0 and n == 0:
        val = ack(m - 1, 1)
    else:
        val = ack(m - 1, ack(m, n - 1))

    # Memorize value with current n and m
    memo[str(m) + str(n)] = val
    return val

# Test small values
print(ack(3, 4))

# Test bigger values (Still doesn't work even with memoization)
# Uncomment to see a RecursionError
# print(ack(40, 50))
