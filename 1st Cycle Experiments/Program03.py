"""
Write a program for swapping of two numbers without using third variable
"""

a, b = map(int, input("Enter two numbers: ").split())

print("Before swap \na =", a, "\nb =", b)
a = a + b
b = a - b
a = a - b
print("After swap \na =", a, "\nb =", b)

"""
OUTPUT
    Enter two numbers: 1 2
    Before swap 
    a = 1 
    b = 2
    After swap 
    a = 2 
    b = 1
"""