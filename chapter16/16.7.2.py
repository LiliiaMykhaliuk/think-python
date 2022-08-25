'''
Exercises of the book "Think python"
16.7.2 Exercise:
'''

# The datetime module provides time objects that are similar to the Time objects in
# this chapter, but they provide a rich set of methods and operators.
# Read the documentation at http://docs.python.org/3/library/datetime.html.
# 
# 1. Use the datetime module to write a program that gets the current date and prints the day of
#     the week.
# 2. Write a program that takes a birthday as input and prints the user’s age and the number of days,
#     hours, minutes and seconds until their next birthday.
# 3. For two people born on different days, there is a day when one is twice as old as the other. That’s
#     their Double Day. Write a program that takes two birth dates and computes their Double Day.
# 4. For a little more challenge, write the more general version that computes the day when one person
#     is n times older than the other.
# Solution: http://thinkpython2.com/code/double.py

from datetime import datetime
from dateutil import relativedelta

# 1

# Set days in week
days_in_week = {
    0 : "Monday",
    1 : "Tuesday",
    2 : "Wednesday",
    3 : "Thursday",
    4 : "Friday",
    5 : "Saturday",
    6 : "Sunday"
}
# Get current date
current_date = datetime.today()

# Get the day of week represented by number (0 - 6)
number_of_day_in_week = current_date.weekday()
# Print the day of week
print(days_in_week.get(number_of_day_in_week))


# 2

# Get the birthday of the user
birthday_str = input("Enter the birthday of the person (dd/mm/yy):")
birthday_time_obj = datetime.strptime(birthday_str, '%d/%m/%Y')
print(birthday_time_obj)

# Get age of the user (the interval in years between two dates)
age = relativedelta.relativedelta(current_date, birthday_time_obj).years
print(age)

# Get the next birthday date
next_birthday =  birthday_time_obj + relativedelta.relativedelta(years=age + 1)

# get and show time to the next birthday
time_to_next_birthday = relativedelta.relativedelta(next_birthday, current_date)

months_bd = time_to_next_birthday.months
days_bd = time_to_next_birthday.days
hours_bd = time_to_next_birthday.hours
minutes_bd = time_to_next_birthday.minutes
seconds_bd = time_to_next_birthday.seconds
print(f"{months_bd} months, {days_bd} days, {hours_bd} hours, {minutes_bd} minutes, {seconds_bd} seconds till your next birthday")


# 3 and 4
# Get the birthday of people

def get_n_times_older_date(birthday_1, birthday_2, n):
    """Finds a date when the oldest person is n-times older than younger person"""

    # Get the older and younger person
    if birthday_1 > birthday_2:
        older_birthday = birthday_2
        younger_birthday = birthday_1
    else:
        older_birthday = birthday_1
        younger_birthday = birthday_2

    # Find a difference between them in days
    diff = relativedelta.relativedelta(younger_birthday, older_birthday).days

    # Get the final date
    days_diff = diff / (n_times_older - 1)
    final_date = younger_birthday + relativedelta.relativedelta(days=days_diff)
    return final_date


# Get people's birthdays
first_birthday_str = input("Enter the birthday of the first person (dd/mm/yy):")
first_birthday = datetime.strptime(first_birthday_str, '%d/%m/%Y')

second_birthday_str = input("Enter the birthday of the second person (dd/mm/yy):")
second_birthday = datetime.strptime(second_birthday_str, '%d/%m/%Y')

# Get how many times person should be older
n_times_older = int(input("How many times older the person has to be? "))

# Get result date
result_date = get_n_times_older_date(first_birthday, second_birthday, n_times_older)
print(result_date)
