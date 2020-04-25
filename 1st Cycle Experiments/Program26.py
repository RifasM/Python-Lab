"""
Write a python program to check whether a given number/string  is palindrome or not.
"""
a = input("Enter a word: ")

if a[::-1] == a:
    print("Palindrome")
else:
    print("Not Palindrome")

"""
OUTPUT
    Enter a word: 12321
    Palindrome
    
    Enter a word: malayalam
    Palindrome
    
    Enter a word: hello
    Not Palindrome
"""