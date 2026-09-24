def load_inventory():
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

load_inventory()