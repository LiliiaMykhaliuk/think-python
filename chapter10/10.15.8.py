'''
Exercises of the book "Think python"
10.15.8 Exercise:
'''
# This exercise pertains to the so-called Birthday Paradox, which you can read about at
# http://en.wikipedia.org/wiki/Birthday_paradox.
# 
# If there are 23 students in your class, what are the chances that two of them have the same
# birthday? You can estimate this probability by generating random samples of 23 birthdays
# and checking for matches. Hint: you can generate random birthdays with the randint
# function in the random module.
# 
# You can download my solution from http://thinkpython2.com/code/birthday.py.


import math
import datetime
import random

# Calculation the chances of not having people with the same birthday
p_minus =  (math.factorial(365) / math.factorial(342)) * (1 / 365)**23

# Calculation of the chances tha two people from 23 will have the same birthday
prob = 1 - p_minus

print(f"The chances of 2 people to have the same birthday among 23 students are: {prob} %")

# Test function

def check_similarity(birthday, others):
    """The function checks amount of same birthdays among others"""

    similar = 0
    for i in others:
        if birthday == i:
            similar += 1

    return similar

def random_birthdays(students = 23):
    """Generates random birthdays"""

    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2000, 12, 1)


    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    birthdays = []

    for i in range(students):

        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        birthdays.append(random_date)
    return birthdays

def test_prob(times):
    """THe function count chances of having same birthday among 23 people"""

    # Counter of people with same birthdays
    count_probability = 0

    for i in range(times):

        same_birthday = 0
        # Generate random birthdays
        birthdays = random_birthdays()
        # Check random birthdays for matches
        for birthday in birthdays:
            same_birthday += check_similarity(birthday, birthdays[birthdays.index(birthday) + 1 :])

        # Count number of times same birthdays were found
        if same_birthday > 0:
            count_probability += 1

    # Return amount of same birthdays
    return (count_probability * 100 ) / times

TIMES = 1000
REAL_PROBABILITY = test_prob(TIMES)
print(f"In {TIMES} simulation of 23 random birthdays, the real percent of found matches was {REAL_PROBABILITY} %")
