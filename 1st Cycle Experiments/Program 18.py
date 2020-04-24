"""
Write a program for string slicing to check if a string can become empty by recursive deletion
"""

string = input("Enter a string: ")
sub = input("Enter the sub string: ")

while len(string) > 0:
    if not string.find(sub) == -1:
        string = string.replace(sub, "", 1)
    else:
        break

if len(string) == 0:
    print("String can become recursively empty")
else:
    print("String cannot become recursively empty")

"""
OUTPUT
    Enter a string: vtvtuu
    Enter the sub string: vtu
    String can become recursively empty
    
    Enter a string: cmrit
    Enter the sub string: cmr
    String cannot become recursively empty
"""