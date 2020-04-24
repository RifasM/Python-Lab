"""
Write a python Program to find the second highest number in an array.
"""

a = list(map(int, input("Enter an array: ").split()))
a.sort(reverse=True)
print("Second highest: ", a[1])

"""
OUTPUT
    Enter an array: 2 20 15 3 1 50
    Second highest:  20
"""