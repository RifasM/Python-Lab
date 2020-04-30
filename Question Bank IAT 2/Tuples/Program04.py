"""
Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

"""

lst = list(tuple(map(int, input().split())) for r in range(int(input('Enter no of tuples: '))))

print([t[:-1] + (100,) for t in lst])

"""
OUTPUT
    Enter no of tuples: 3
    10 20 40
    40 50 60
    70 80 90
    [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""