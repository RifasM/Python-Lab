"""
Write a python program to check whether a given number is Armstrong number of not. (Eg: 153, 371, 1634…)
"""

num = input("Enter a number: ")
sum = 0

for i in num:
    sum = sum + int(i)**len(num)

if sum == int(num):
    print(num, "is Armstrong")
else:
    print(num, "is not Armstrong")

"""
OUTPUT
    Enter a number: 153
    153 is Armstrong
    
    Enter a number: 371
    371 is Armstrong
    
    Enter a number: 123
    123 is not Armstrong
"""