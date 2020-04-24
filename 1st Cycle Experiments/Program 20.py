"""
Write a program to check whether the given year is a leap year or not.
"""

year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is a leap year")
else:
    print("The year isn't a leap year")

"""
OUTPUT
    Enter year: 2020
    The year is a leap year
    
    Enter year: 2003
    The year isn't a leap year
"""