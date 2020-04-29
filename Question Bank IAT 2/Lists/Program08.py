"""
Write a Python program to get the frequency of the elements in a list.
"""

lst = input("Enter a list: ").split()

count = {}

for a in lst:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

for a in count.keys():
    print("Frequency of", a, " = ", count[a])

"""
OUTPUT
    Enter a list: 1 2 a 2 a b
    Frequency of 1  =  1
    Frequency of 2  =  2
    Frequency of a  =  2
    Frequency of b  =  1
"""