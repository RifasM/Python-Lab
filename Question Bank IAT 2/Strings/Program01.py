"""
Write a python program to print the sum of the ASCII value of all characters of the input string.
"""

string = input("Enter a string: ")

sum = 0
for i in string:
    print("ASCII value of", i, "is", ord(i))
    sum = sum + ord(i)

"""
OUTPUT
    Enter a string: Hello
    ASCII value of H is 72
    ASCII value of e is 101
    ASCII value of l is 108
    ASCII value of l is 108
    ASCII value of o is 111
"""