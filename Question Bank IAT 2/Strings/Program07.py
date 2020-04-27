"""
Write a program to check if the Substring is Present in a Given String
"""

string = input("Enter a string: ")
sub = input("Enter Substring: ")

if sub in string:
    print("Substring present")
else:
    print("Substring not present")

"""
OUTPUT
    Enter a string: Hello World
    Enter Substring: ello
    Substring present

    Enter a string: CMRIT
    Enter Substring: VTU
    Substring not present
"""