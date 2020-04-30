"""
Write a Python program to reverse a tuple.
"""

print("Reversed: ", tuple(reversed(tuple(input("Enter a tuple: ")[1:-1]))))

"""
OUTPUT
    Enter a tuple: (12345)
    Revered:  ('5', '4', '3', '2', '1')
"""
