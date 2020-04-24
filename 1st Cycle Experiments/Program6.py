"""
Print the following pattern
1
1 1
1 1 1
"""

n = int(input("Enter number of lines: "))

for i in range(n):
    for j in range(i+1):
        print(1, end=" ")
    print('')

"""
OUTPUT
    Enter number of lines: 3
    1 
    1 1 
    1 1 1 
"""
