"""
Write a  python program to read the contents of the file in reverse order.
"""

from create import createFile

fname = input("Enter file name: ")
createFile(fname, "Hello\nWorld\nThis is a Test File")

with open(fname+".txt", "r") as f:
    for line in reversed(f.readlines()):
        print(line.rstrip())

"""
OUTPUT
    Enter file name: file
    This is a Test File
    World
    Hello
"""