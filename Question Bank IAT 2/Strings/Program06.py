"""
Write a program to check if two given strings are anagram or not.
"""

a, b = map(str, input("Enter two strings: ").split())

if len(a) != len(b):
    print("Not Anagrams")
else:
    a = sorted(a)
    b = sorted(b)
    for i in range(0, len(a)):
        if a[i] != b[i]:
            print("Not Anagrams")
            exit(0)
    print("Anagrams")

"""
OUTPUT
    Enter two strings: abc cba
    Anagrams

    Enter two strings: ABCD ABDEF
    Not Anagrams
"""