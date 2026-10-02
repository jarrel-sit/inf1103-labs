#Imports
import json
import os

products = []



def add_product():
    new_id = input("Enter new product ID: ")
    new_name = input("Enter product name: ")
    new_price = input("Enter product price: ")
    new_quantity = int(input("Enter product quantity: "))
    products.append({"ID": new_id, "details": [new_name, new_price, new_quantity]})

#def load_inventory():

