"""
Write a program in python to print the file contents with line number using file.
"""

from create import createFile

fname = input("Enter file name: ")
createFile(fname, "Hello\nWorld\nThis is a Test File")

with open(fname+".txt", "r") as f:
    i = 1
    for line in f:
        print("Line No.", i, "Content:", line)
        i += 1

"""
OUTPUT
    Enter file name: file
    Line No. 1 Content: Hello
    
    Line No. 2 Content: World
    
    Line No. 3 Content: This is a Test File
"""