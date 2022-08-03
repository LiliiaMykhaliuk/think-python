'''
Exercises of the book "Think python"
10.15.2 Exercise:
'''

# Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
# that is, a new list where the ith element is the sum of the first i+1 elements from the original
# list. For example:
# 
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

def cumsum(in_list):
    """Function returns the cumulative sum of the numbers in list"""

    # List of cumulative sum
    sum_list = []

    # Get the first element without summing since previous value doesn't exist 
    sum_list.append(in_list[0])

    #Get the sum for each element
    for i in range(1, len(in_list)):

        sum_list.append(sum_list[i - 1] + in_list[i])

    return sum_list

print(cumsum([1, 4, 6]))

print(cumsum([1, 2, 3]))

print(cumsum([1, 1, 1, 1, 1, 1]))
