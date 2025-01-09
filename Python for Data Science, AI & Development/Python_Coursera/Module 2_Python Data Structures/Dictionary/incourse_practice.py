# Scenario:Inventory Store
# The inventory store scenario project utilizes a dictionary-based approach to develop a robust system for managing and tracking inventory in a retail store.
# Note:- You will be working with two product details.

# Task-1 Create an empty dictionary
# First you need to create an empty dictionary, where you will be storing the product details.

Inventory_dict={}

# Task-2 Store the first product details in variable
# Product Name= Mobile phone
# Product Quantity= 5
# Product price= 20000
# Product Release Year= 2020

Product1= "Mobile phone"
Quantity= 5
price= 20000
Release1= 2020

# Task-3 Add the details in inventory

Inventory_dict["Product1"]=Product1
Inventory_dict["Quantity"]=Quantity
Inventory_dict["price"]=price
Inventory_dict["Release1"]=Release1

# Task-4 Store the second product details in a variable.
# Product Name= "Laptop"
# Product Quantity= 10
# Product price = 50000
# Product Release Year= 2023

Product2= "Laptop"
Quantity2= 10
price2= 50000
Release2= 2023

#Task-5 Add the item detail into the inventory.

Inventory_dict["Product2"]=Product2
Inventory_dict["Quantity2"]=Quantity2
Inventory_dict["price2"]=price2
Inventory_dict["Release2"]=Release2

#Task-6 Display the Products present in the inventory¶

print(Inventory_dict)

#Task-7 Check if ProductNo1_releaseYear and ProductNo2_releaseYear is in the inventory

"Release" in Inventory_dict
"Release2" in Inventory_dict
print(Inventory_dict)

#Task-8 Delete release year of both the products from the inventory

del(Inventory_dict["Release1"])
del(Inventory_dict["Release2"])

print(Inventory_dict)