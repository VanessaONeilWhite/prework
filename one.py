# Question 1
from operator import truediv


def hello_name(user_name):
    """Display username"""
    print("hello_" + user_name + "!")

hello_name("USERNAME")

# Question 2
first_odds = list(range(1, 100, 2))
print(first_odds)

def first_odds():
    print(" ")

# Question 3
def max_num_in_a_list(a_list):
    """print max number"""
a_list = [8, 6, 7, 5, 3, 0, 9]
max_number = max(a_list); 

print(max_number)

# Question 4 
def is_leap_year(a_year):
    """print if it is a leap year"""

    if a_year % 400 == 0:
        leap = True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        leap = True 
    else:
        leap = False
    return leap

a_year = 2022
print(is_leap_year(a_year))

# Question 5
def is_consecutive(a_list):
    """ see if numbers are consecutive"""
    return sorted(a_list) == list(range(min(1), max(1)+1))
a_list = [8, 6, 7, 5, 3, 0, 9]

print(is_consecutive(a_list))