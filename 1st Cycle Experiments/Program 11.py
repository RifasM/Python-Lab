"""
Write a program to compare two numbers without using relational operator
"""

a, b = map(int, input("Enter two numbers: ").split())
if not a ^ b == 0:
    print("Not equal")
else:
    print("Equal")

"""
OUTPUT
    Enter two numbers: 3 52
    Not equal
    
    Enter two numbers: 50 50
    Equal
"""