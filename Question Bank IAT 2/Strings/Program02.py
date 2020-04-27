"""
Write a program to slice a string into 3 equal parts. Input string contains a single word.
Display each slice of the original string.
"""

string = input("Enter a sentence: ")

s = len(string)

if s % 3 == 0:
    p = s / 3
    k = 0
    for i in string:
        if k % p == 0:
            print()
        print(i, end='')
        k += 1

"""
OUTPUT
    Enter a sentence: EnterASentence:

    Enter
    ASent
    ence:
"""