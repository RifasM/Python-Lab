"""
Write a Python program to remove duplicates from a list.
"""

[print(a, end=" ") for a in list(dict.fromkeys(input("Enter a list of elements to remove duplicates: ").split()))]

"""
OUTPUT
    Enter a list of elements to remove duplicates: 1 4 2 4 1 4 52 5
    1 4 2 52 5 
"""