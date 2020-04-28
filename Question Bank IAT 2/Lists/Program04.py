"""
Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""

lst = list(map(int, input("Enter List: ").split()))
for a in lst:
    if a % 2 == 0:
        lst = list(filter(a.__ne__, lst))


print("Even numbers removed:", lst)

"""
OUTPUT
    Enter List: 1 2 3 4 5 6
    Even numbers removed: [1, 3, 5]
"""