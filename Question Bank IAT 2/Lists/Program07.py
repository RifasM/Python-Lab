"""
Write a Python program to append a list to the second list.
"""

lst1 = input("Enter list 1: ").split()
lst2 = input("Enter list 2: ").split()

[lst2.append(a) for a in lst1]

print("List 1 appended to List 2")
print("List 1:", lst1, "\nList 2:", lst2)

"""
OUTPUT
    Enter list 1: 1 2 3
    Enter list 2: a b c
    List 1 appended to List 2
    List 1: ['1', '2', '3'] 
    List 2: ['a', 'b', 'c', '1', '2', '3']
"""