"""
Write a program to find the transpose of a matrix.
"""

row = int(input("Enter no. of rows: "))
col = int(input("Enter no. of columns: "))

mat = []

print("Enter the matrix: ")
for i in range(row):
    mat.append(list(map(int, input().split())))

print("Transposed matrix: ")
for i in range(row):
    for j in range(col):
        print(mat[j][i], end=' ')
    print()

"""
OUTPUT
    Enter no. of rows: 2
    Enter no. of columns: 2
    Enter the matrix: 
    1 2
    3 4
    Transposed matrix: 
    1 3 
    2 4 
"""