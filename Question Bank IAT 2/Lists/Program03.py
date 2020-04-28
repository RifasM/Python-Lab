"""
Write a Python function that takes two lists and returns True if they have at least one common member.
"""


def common(a, b):
    for i in a:
        if i in b:
            return True
    return False


lst1 = input("Enter List 1: ").split()
lst2 = input("Enter List 2: ").split()

print(common(lst1, lst2))

"""
OUTPUT
    Enter List 1: 1 2 3 4 5
    Enter List 2: 5 6 7 8 9
    True
    
    Enter List 1: 1 2 3 4 5
    Enter List 2: 6 7 8 9 0
    False
"""