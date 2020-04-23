"""
Write a python program to sum of N natural numbers[even,odd,divisible by n]
"""

num = map(int, input("Enter N natural numbers: ").split())
sum = 0

for a in num:
    if a > 0:
        sum = sum + a
    else:
        print("Enter positive numbers")
        exit(0)

print("Sum of is", sum)

"""
OUTPUT:
    Enter N natural numbers: 1 2 3 4 5 6 7 8 9 10
    Sum of is 55
    
    Enter N natural numbers: 12 31 -1 02 20 22
    Enter positive numbers
"""