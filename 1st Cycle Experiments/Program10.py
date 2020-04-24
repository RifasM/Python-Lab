"""
Write a python program to generate Fibonacci number up to 50
"""
import math

low, high = map(int, input("Enter the range: ").split())


def isPerfectSquare(x):
    return math.sqrt(x) - math.floor(math.sqrt(x)) == 0


for i in range(low, high):
    if isPerfectSquare(5*i*i + 4) or isPerfectSquare(5*i*i - 4):
        print(i)

"""
OUTPUT
    Enter the range: 10 50
    13
    21
    34
"""