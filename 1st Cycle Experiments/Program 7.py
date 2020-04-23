"""
Write a program to reverse an array without using another array
"""

arr = list(map(int, input("Enter an array of elements: ").split()))

print("Before reverse: ", arr)
s = 0
e = len(arr)-1

while s < e:
    arr[s], arr[e] = arr[e], arr[s]
    s = s + 1
    e = e - 1

print("After reverse: ", arr)

"""
OUTPUT
    Enter an array of elements: 1 2 3 4 5 6
    Before reverse:  [1, 2, 3, 4, 5, 6]
    After reverse:  [6, 5, 4, 3, 2, 1]
"""
