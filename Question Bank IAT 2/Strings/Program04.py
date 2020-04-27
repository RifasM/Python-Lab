"""
Write a program to reverse only words in a string.
"""

[print(i, end=' ') for i in input("Enter a sentence: ").split()[::-1]]

"""
OUTPUT
    Enter a sentence: I Love Cmrit
    Cmrit Love I 
"""