"""
Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30 (both included).
"""

low, high = map(int, input("Enter range: ").split())
lst = []
for i in range(low, high+1):
    lst.append(i**2)
print("First 5:", lst[:5])
print("Last 5:", lst[-5:])

"""
OUTPUT
    Enter range: 10 20
    First 5: [100, 121, 144, 169, 196]
    Last 5: [256, 289, 324, 361, 400]
"""