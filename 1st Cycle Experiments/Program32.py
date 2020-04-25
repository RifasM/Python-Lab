"""
Write a python function to check whether three given numbers can form the sides of a triangle.
"""


def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print(a, ",", b, ",", c, "form a triangle")
    else:
        print(a, ",", b, ",", c, "do not form a triangle")


p, q, r = map(int, input("Enter sides of triangle: ").split())
triangle(p, q, r)

"""
OUTPUT
    Enter sides of triangle: 2 2 10
    2 , 2 , 10 form a triangle
    
    Enter sides of triangle: 10 10 10
    10 , 10 , 10 do not form a triangle
"""