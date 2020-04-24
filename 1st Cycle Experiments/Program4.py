"""
Write a python program to print all prime numbers in given range. ex. (1,100)
"""

lower, upper = map(int, input("Enter two numbers: ").split())


def isPrime(a):
    if a <= 1:
        return
    else:
        c = 0
        for j in range(2, a):
            if a % j == 0:
                c = c + 1
        if c == 0:
            print(a)


for i in range(lower, upper):
    isPrime(i)

"""
OUTPUT
    Enter two numbers: 1 10
    2
    3
    5
    7
"""