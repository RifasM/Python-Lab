"""
You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z.
The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins.
How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.
"""

z = int(input("Enter amount: "))
x = int(input("Enter no. of 5 rupee coins: "))
y = int(input("Enter no. of 1 rupee coins: "))
num = 0

num = z // 5
z = abs((num*5) - z)

if num > x or z > y:
    print("-1")
else:
    print("No. of 5 rupee coins:", num)
    print("No. of 1 rupee coins:", z)

"""
OUTPUT
    Enter amount: 24
    Enter no. of 5 rupee coins: 5
    Enter no. of 1 rupee coins: 6
    No. of 5 rupee coins: 4
    No. of 1 rupee coins: 4
    
    Enter amount: 50
    Enter no. of 5 rupee coins: 9
    Enter no. of 1 rupee coins: 3
    -1
"""