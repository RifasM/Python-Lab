"""
Write a program to sort an array
"""

arr = list(map(int, input("Enter an array of elements: ").split()))

newarr = arr

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Without Built in:", arr)
newarr.sort()
print("Using Built in:", newarr)

"""
OUTPUT:
    Enter an array of elements: 100 15 2 14 1
    Without Built in: [1, 2, 14, 15, 100]
    Using Built in: [1, 2, 14, 15, 100]
"""
