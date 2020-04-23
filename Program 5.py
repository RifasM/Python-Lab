"""
Write a python program to print the string until the input letter is found.
"""

letter = input("Enter the input letter(delimiter): ")
string = input("Enter the string: ")

print("Delimited String: ", end="")
for a in string:
    if a == letter:
        break
    print(a, end="")

"""
OUTPUT
    Enter the input letter(delimiter): 0
    Enter the string: Hello W0rld
    Delimited String: Hello W
"""