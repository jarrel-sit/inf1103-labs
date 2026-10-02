#Imports
import json
import os

products = []


#Function for adding new products
def add_product():
    #Initializing ID and details about product
    new_id = input("Enter new product ID: ")

    #Checks if product ID already exists
    for product in products:
        if new_id == product['ID']:
            print("Invalid Product ID, Product ID already exists.")
            return

    #If Product ID does not exist yet, continue with other fields
    new_name = input("Enter product name: ")
    new_price = input("Enter product price: ")
    new_quantity = int(input("Enter product quantity: "))

    #Adds new product to product list
    products.append({"ID": new_id, "details": [new_name, new_price, new_quantity]})

#Function for loading inventory
def display_all():
    #Returns information about product(s) if array of products added so far is not empty
    if len(products) != 0:
        for product in products:
            print(f" ID: {product["ID"]} | Name: {product["details"][0]} | Price: {product["details"][1]} | Stock: {product["details"][2]}")

    #Informs user that inventory is empty
    else:
        print("Inventory is Empty")

#Function for searching product
def search_product():
    print("Search Product")
    #Asks user for Product ID that they are looking for
    find = input("Enter Product ID: ")

    #Checks product in products array and returns details of product if ID is matching
    for product in products:
        if find == product['ID']:
            print("Product Found:")
            print(f"Name: {product["details"][0]} \nCurrent Stock: {product["details"][2]}")
            break

    #Returns message if product was not found
    else:
        print("Product Not in Inventory")

#Function to Update Stock of Products
def update_stock():
    print("Update Stock")
    #Asks user which product ID to update quantity 
    update = input("Enter Product ID: ")

    #Looks for product if matching ID, shows user current quantity
    for product in products:
        if update == product['ID']:
            print(f"\nProduct Found: \nName:{product["details"][0]} \nCurrent Stock: {product["details"][2]}")

            #Asks user for new stock quantity, replaces it 
            try:
                newstock = int(input("New Stock Quantity: "))
                product["details"][2] = newstock
                break
            #If user inputs something that is not a number, returns error message
            except ValueError:
                print("Invalid New Quantity")
    else:
        print("Unable to update quantity")



def menu():
    while True:
        print("\n----------- MENU -----------\n1. Add Product\n2. Load Inventory\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit\n----------------------------")
        choice = input("\nEnter option:")
        #Runs functions based on user's option
        if choice == '1':
            add_product()
        elif choice == '2':
            display_all()
        elif choice == '3':
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        #Saves and exits program
        elif choice == "6":
            print("Saving inventory before exit...\nInventory saved successfully.\n\nThank you for using Inventory Management System.\nProgram terminated.")
            with open("inventory.json", "w") as file:
                json.dump(products, file)
            break
        #Returns error message if invalid choice
        else:
            print("Invalid choice. Please try again.")

#Function to save inventory
def save_inventory():
    print("Saving inventory...\nInventory saved successfully to inventory.json")
    with open("inventory.json", "w") as file:
        json.dump(products, file)

#Loads inventory if exists
file_path = "inventory.json"
if os.path.isfile(file_path):
    print("inventory.json found.\nInventory loaded successfully.")
    with open('inventory.json', 'r') as file:
        data = json.load(file)
        for i in data:
            products.append(i)

#Main Function to run menu
menu()