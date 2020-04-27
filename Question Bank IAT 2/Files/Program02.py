"""
Write a python program  to append the contents of one file to another file.
"""

from create import createFile

fname1 = input("Enter file 1 name: ")
createFile(fname1, "Hello\nWorld\nThis is a Test File")

fname2 = input("Enter file 2 name: ")
createFile(fname2, "This is a Test File for appending")

with open(fname2+".txt", "a") as f2:
    with open(fname1+".txt", "r") as f1:
        f2.write(f1.read())

print("Appended '", fname1, "' contents to '", fname2, "'\nFile:")

with open(fname2+".txt", "r") as f:
    print(f.read())

"""
OUTPUT
    Enter file 1 name: file
    Enter file 2 name: append
    Appended ' file ' contents to ' append '
    File:
    This is a Test File for appendingHello
    World
    This is a Test File

"""
