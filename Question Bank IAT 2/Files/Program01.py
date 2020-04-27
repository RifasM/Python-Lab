"""
Write a program in python to count the number of lines in a text file.
"""
from create import createFile

fname = input("Enter File Name: ")
createFile(fname, "Hello\nWorld\nThis is a Test File")
with open(fname+".txt", "r") as f:
    count = 0
    for line in f:
        count = count + 1
    print("No. of lines in file.txt:", count)

"""
OUTPUT
    Enter File Name: file
    No. of lines in file.txt: 3
"""