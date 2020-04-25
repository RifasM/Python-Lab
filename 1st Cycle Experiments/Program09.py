"""
Write a program to find how many nodes are there in Level 4 of binary tree.
"""

level = int(input("Enter level: "))

print("No of nodes at level", level, ": ", 2**(level-1))

"""
OUTPUT
    Enter level: 4
    No of nodes at level 4 :  8
"""