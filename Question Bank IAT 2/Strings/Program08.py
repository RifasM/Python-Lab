"""
Write a program to count vowels in a given string.
"""

import re

print(len(re.findall("[aeiouAEIOU]", input("Enter a string: "))))

"""
OUTPUT
    Enter a string: Hello World
    3
"""