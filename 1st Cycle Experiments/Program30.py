"""
Write a python program to check entered number is perfect number or not.
"""

a = int(input("Enter a number: "))
sum = 0

for i in range(1, a):
    if a % i == 0:
        sum = sum + i

if sum == a:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

"""
OUTPUT
    Enter a number: 6
    The number is a Perfect number
    
    Enter a number: 12
    The number is not a Perfect number
"""