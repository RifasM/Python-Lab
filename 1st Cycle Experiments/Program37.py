"""
Write a python program to find and display the product of three positive integer values based on the rule mentioned below:
It should display the product of the three values except when one of the integer value is 7.
In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself.
If no values can be included in the product, display -1.
"""

num1, num2, num3 = map(int, input("Enter three numbers: ").split())

res = 0
if num1 != 7 and num2 != 7 and num3 != 7:
    res = num1 * num2 * num3
elif num1 == 7 and num2 == 7 and num3 == 7:
    res = '-1'
elif num1 == 7:
    res = num2 * num3
elif num2 == 7:
    res = num3
elif num3 == 7:
    res = -1

print("Product of ", [num1, num2, num3], " = ", res, end='')

"""
OUTPUT
    Enter three numbers: 1 7 2
    Product of  [1, 7, 2]  =  2
    
    Enter three numbers: 1 5 3
    Product of  [1, 5, 3]  =  15
    
    Enter three numbers: 7 7 7 
    Product of  [7, 7, 7]  =  -1
"""