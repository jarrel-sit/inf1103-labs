#Function to get valid input from user
def get_valid_input():
    user_input = input("Would you like to add stock or quit? ").lower()
    #Returns quit to exit the program and print out report
    if user_input == "quit":
        return ("quit")
    #Handles invalid inputs + Enforce business rule (stock quantity cannot be negative)
    elif not user_input.isdigit():
        print("Invalid input. Please enter a valid non-negative number.")
        return(user_input)
    #Returns valid integer amount to be added to inventory
    else:
        return(user_input) 

#Function to show user the current inventory amount before tax is applied
def process_delivery(user_input,inventory):
    #Adds user_input to inventory amount
    if user_input.isdigit():
        inventory += int(user_input)
        #Shows user the current inventory amount before tax is applied
        print(f"Before tax, you have {inventory} stock")
        return inventory

#Function to calculate tax based on the amount of stock being added
def calculate_tax(amount):
    if amount >= 10:
        tax = round(amount * 0.1)
    else:
        tax = 0
    return tax 

#Function to generate a report of total units processed and failed attempts
def generate_report(total_units, failed_attempts):
    print(f"\nNumber of successful orders: {valid} \nTotal units processed: {total_units} \nFailed_attempts: {failed_attempts}")

#Initialize inventory, valid and invalid attempts
inventory = 0
invalid = 0
valid = 0

#Main loop to continuously ask user for stock quantity until they type quit
while True:
    #Runs the user input function to get input from the user
    user_input = get_valid_input()
    #If the user input is a digit, process the delivery and calculate tax
    if user_input.isdigit():
        valid +=1
        inventory = process_delivery(user_input,inventory)
        tax = calculate_tax(int(user_input))
        #Output the delivery amount before tax is applied and the taxed amount
        print(f"Order No. {valid} of {user_input} has been processed")
        inventory = inventory - tax
        #Output the total units after tax is applied
        print(f"Order No. {valid} has been taxed {tax} units. After tax, your current stock is: {inventory} unit(s) \n")

    #Breaks the loop and generates a report if the user types quit
    elif user_input == "quit":
        generate_report(inventory, invalid) 
        break
    #Adds 1 to invalid attempts if the user input is not a digit and continues the loop
    elif user_input.isdigit() == False:
        invalid += 1
        continue





