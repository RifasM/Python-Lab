"""
Write a program to remove duplicates from an array
"""

arr = list(map(int, input("Enter array: ").split()))
newarr = []

for a in arr:
    if a not in newarr:
        newarr.append(a)

arr = newarr
print("Formatted array: ", arr)

"""
OUTPUT
    Enter array: 2 2 5 6 2 4 20
    Formatted array:  [2, 5, 6, 4, 20]
"""