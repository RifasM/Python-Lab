"""
Write a python program to find HCF of two numbers.
"""

a, b = map(int, input("Enter two numbers: ").split())


def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)


print("GCD of", a, "and", b, "is:", gcd(a, b) or "Error")

"""
OUTPUT
    Enter two numbers: 12 6
    GCD of 12 and 6 is: 6
    
    Enter two numbers: 13 24
    GCD of 13 and 24 is: 1
"""