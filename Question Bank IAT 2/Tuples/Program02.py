"""
Write a Python program to convert a tuple to a dictionary.
"""

t = list(tuple(map(int, input().split())) for r in range(int(input('Enter no of tuple pairs : '))))

a = dict((y, x) for x, y in t)
print("Dictionary:\n", a)

"""
OUTPUT
    Enter no of tuple pairs : 2
    1 2
    3 4
    Dictionary:
     {2: 1, 4: 3}
"""