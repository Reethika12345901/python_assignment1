print("welcome to our cafeteria!")
name=input("enter your name")
mobile_num=int(input("enter the mobile number"))
print("done!")
print("check out below food items")
# list of items!
list="""pizza,
burger,
pancakes,
popcorn,
cheese burger coffee,
chocolate cake,
sausage,
Brownie,
coold drinks,
veg puff,
egg puff,
chicken puff,
noodles"""
#cost of list of items:
price="""pizza:100
burger:80
pancakes:60
popcorn:45
cheese_burger:130
coffee:50
chocolate:70
cake:58
cool drinks:30
egg puff : 40
chicken puff:60
veg puff: 30
sausage:80
brownie:120
noodles:60
"""
#list of items enter by user
items=(input("enter the item of above list:"))
#price of each item
items_price=int(input("enter the item prize:"))
#quantity of food items
quantity=int(input("enter the quantity of items:"))
#steps for finding GST
#multiply item_price and quantity
list=items_price*quantity
#finding GST
GST=list*18/100
#calculating total price with GST
total_price=list+GST
print("original cost with gst amount:",total_price)
print("thank you happy customer:")
print("visit again",end="!")