"""
Write a python program to counting digits in number with floor division
"""

n = int(input("Enter a number: "))

count = 0
while n != 0:
    n //= 10
    count += 1

print("No. of digits:", count)

"""
OUTPUT
    Enter a number: 123
    No. of digits: 3
"""