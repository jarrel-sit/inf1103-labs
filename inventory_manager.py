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

def load_inventory():
    print("Current Inventory \n ------------------------------------------------")
    for product in products:
        print(f"ID: {product['ID']} | Name: {product['details'][0]} | Price: {product['details'][1]} | Quantity: {product['details'][2]}")
    print ("------------------------------------------------")

def menu():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Load Inventory")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            load_inventory()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

menu()