"""
Write a python program to count the number of vowels and consonants in a file.
"""

from create import createFile
import re

fname = input("Enter file name: ")
createFile(fname, "Hello\nWorld\nThis is a Test File")

with open(fname+".txt", "r") as f:
    f = f.read().replace(" ", "").replace("\n", "").replace("\t", "")
    print(f)
    vow = len(re.findall('[aeiouAEIOU]', f))
    print("Vowel Count:", vow)
    print("Consonant Count:", len(f)-vow)

"""
OUTPUT
    Enter file name: file
    HelloWorldThisisaTestFile
    Vowel Count: 9
    Consonant Count: 16
"""