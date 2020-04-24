"""
Write a python program to find the sum of x+x2/2+x3/3+…..+xn/n
"""

n = int(input("Enter the number of terms:"))
x = int(input("Enter the value of x:"))
sum = 1
for i in range(2, n+1):
    sum = sum + ((x**i)/i)
    print('('+str(x)+'^'+str(i)+')'+'/'+str(i)+' =', str((x**i)/i))
print("\nThe sum of series is", round(sum, 4))

"""
OUTPUT
    Enter the number of terms:5
    Enter the value of x:2
    (2^2)/2 = 2.0
    (2^3)/3 = 2.6666666666666665
    (2^4)/4 = 4.0
    (2^5)/5 = 6.4
    
    The sum of series is 16.0667
"""