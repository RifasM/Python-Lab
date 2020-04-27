"""
Write a python program to read an input string from the user.
Remove the white spaces from the input string and display it.
Also retrieve the characters at the odd index from this string and form a new string and display it.
"""

string = input("Enter a string: ")
news = string.replace(" ", "")
print("Whitespace removed:", news)
print("Odd index string: ", end='')
[print(news[i], end='') for i in range(1, len(string), 2)]

"""
OUTPUT
    Enter a string: Hello World
    Whitespace removed: HelloWorld
    Odd index string: elWrd
"""