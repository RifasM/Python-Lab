"""
Write a python program to calculate factorial of given number.
"""


def fact(a):
    if a == 1:
        return 1
    else:
        return a*fact(a-1)


print("Factorial: ", fact(int(input("Enter a number: "))))

"""
OUTPUT
    Enter a number: 6
    Factorial:  720
"""