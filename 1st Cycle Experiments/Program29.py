"""
Write a python program to find LCM of two numbers
"""

a, b = map(int, input("Enter two numbers: ").split())


def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)


print("LCM of", a, "and", b, "is:", (a * b) // gcd(a, b) or "Error")

"""
OUTPUT
    Enter two numbers: 5 6
    LCM of 5 and 6 is: 30
"""