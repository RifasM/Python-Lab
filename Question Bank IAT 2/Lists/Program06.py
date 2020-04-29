"""
Write a Python program to generate all permutations of a list in Python.
"""

a = input("Enter a list: ").split()


def permute(c, start, end):
    if start == end:
        print(' '.join(c))
    else:
        for i in range(start, end + 1):
            c[start], c[i] = c[i], c[start]
            permute(c, start + 1, end)
            c[start], c[i] = c[i], c[start]


permute(a, 0, len(a)-1)

"""
OUTPUT
    Enter a list: hello 1 2
    hello 1 2
    hello 2 1
    1 hello 2
    1 2 hello
    2 1 hello
    2 hello 1
"""