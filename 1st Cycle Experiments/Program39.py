"""
FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.
A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate.
Their non-veg combo is really famous that they get more orders for their non-vegetarian combo
than the vegetarian combo. Apart from the cost per plate of food, customers are also charged
for home delivery based on the distance in kms from the restaurant to the delivery point.
The delivery charges are as mentioned below:

Distance in kms	    Delivery charge in Rs. Per kms
For first 3kms	            0
For next 3kms	            3
For the remaining	        6

Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant
to the delivery point, write a python program to calculate the final bill amount to be paid by a customer.
The below information must be used to check the validity of the data provided by the customer:
•	Type of food must be ‘V’ for vegetarian and ‘N’ for non-vegetarian.
•	Quantity ordered should be minimum 1.
•	Distance in kms must be greater than 0.
If any of the input is invalid, the bill amount should be considered as -1

"""

t = input("Enter Vegetarian(V) or Non-Vegetarian(N): ")
q = int(input("Enter Quantity: "))
d = int(input("Enter distance in km: "))
if t not in ['V', 'v', 'N', 'n'] or q < 1 or d == 0:
    print("Bill amount: -1")
else:
    amt = 0
    if t in ['V', 'v']:
        amt = 120*q
    else:
        amt = 150*q
    if d > 6:
        amt = amt + 9 + (d-6)*6
    elif 3 < d < 6:
        amt = amt + (d-3)*3
    print("Bill Amount:", amt)

"""
OUTPUT
    Enter Vegetarian(V) or Non-Vegetarian(N): n
    Enter Quantity: 2
    Enter distance in km: 4
    Bill Amount: 303
    
    Enter Vegetarian(V) or Non-Vegetarian(N): v
    Enter Quantity: 0
    Enter distance in km: 4
    Bill amount: -1
"""