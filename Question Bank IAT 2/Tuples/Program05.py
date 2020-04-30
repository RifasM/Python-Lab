"""
Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

"""

lst = list(tuple(input().split()) for r in range(int(input('Enter no of tuples: '))))
print(sorted(lst, key=lambda x: float(x[1]), reverse=True))

"""
OUTPUT
    Enter no of tuples: 3
    item1 12.20
    item2 15.10
    item3 24.5
    [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""