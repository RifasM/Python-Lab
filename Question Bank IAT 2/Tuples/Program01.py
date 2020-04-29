"""
Write a Python program to find the repeated items of a tuple.
"""

tup = tuple(input("Enter a tuple: "))
d = {}
for a in tup:
    if a not in [" ", "\n", ", ",","]:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

print("Repeated Items: ")
for a in d.keys():
    if int(d[a]) != 1:
        print(a)

"""
OUTPUT
    Enter a tuple: 1, 2, 3, 1, 4, 3
    Repeated Items: 
    1
    3
"""
