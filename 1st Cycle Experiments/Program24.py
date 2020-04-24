"""
Write a python program to calculate the sum of digits of a number.
"""

num = input("Enter a number: ")

sum = 0
for i in num:
    sum = sum + int(i)

print("Sum:", sum)

"""
OUTPUT
    Enter a number: 123
    Sum: 6
"""