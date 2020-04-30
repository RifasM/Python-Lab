"""
Write the following functions:
•   create(k1,k2,k3,k4,v1,v2,v3,v4), that creates a dictionary d={k1:v1,k2:v2k3:v3k4:v4} and returns a dictionary.
•	display(), that displays key along with its price and stock information.
•	If_all_sold(), that displays the total amount if all the goods are sold.
•	max_stock(), that displays the product that is in maximum stock.
•	max_price(), that displays the product with maximum price.

"""


def create(lst):
    l1 = lst[0:len(lst)//2]
    l2 = lst[len(lst)//2:]
    d = dict(zip(l1, l2))
    return d


def if_all_sold(item_name):
    if stock[item_name] == 0 or None:
        return True
    else:
        return False


def max_stock():
    return max(stock)


def max_price():
    return max(prices, key=prices.get)


def display():
    print("Item\tStock\tPrice")
    for i in stock.keys():
        print(i, "\t", stock[i], "\t", prices[i])


stock = create(['radish', 'apple', 'tomato', 5, 2, 10])
prices = create(['radish', 'apple', 'tomato', 50, 100, 30])

print("All Products")
display()

print("Maximum Priced product:", max_price())
print("Maximum stocked product:", max_stock())
print("Are all the Tomatoes sold?", if_all_sold('tomato'))

"""
OUTPUT
    All Products
    Item	Stock	Price
    radish 	 5 	     50
    apple 	 2 	    100
    tomato 	 10 	 30
    Maximum Priced product: apple
    Maximum stocked product: tomato
    Are all the Tomatoes sold? False
"""