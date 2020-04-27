"""
Write a program to find a Permutation of a given string (Printing various combinations of characters in the string).
"""

a = list(input("Enter a string: "))


def permute(c, start, end):
    if start == end:
        print(''.join(c))
    else:
        for i in range(start, end + 1):
            c[start], c[i] = c[i], c[start]
            permute(c, start + 1, end)
            c[start], c[i] = c[i], c[start]


permute(a, 0, len(a)-1)

"""
OUTPUT
    Enter a string: vtu
    vtu
    vut
    tvu
    tuv
    utv
    uvt
"""