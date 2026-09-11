#Auditor Function
def auditor():
    #Initialize inventory to zero in the start
    inventory = 0
    invalid = 0
    #Run in a continuous loop asking user to enter a stock quantity, until the user types quit.
    while True: 
        user = input("Stock Quantity: ").lower()
        #Reporting (if the user types quit, print the total number of units processed and the number of failed/rejected entries)
        if user == "quit":
            print("Total Units Processed: ", inventory)
            print("Number of Failed/Rejected Entries: ", invalid)
            return False
        
        #Handle invalid inputs + Enforce business rule (stock quantity cannot be negative)
        elif user.isdigit() == False:
            print("Invalid input. Please enter a valid non-negative number.")
            invalid += 1
            continue

        #Accept stock values as integers
        else:
            inventory += int(user)
            #Manage state (Running total of stock quantity)
            print(f"Current inventory: {inventory}")
            
        #Trigger overstock alert (if the inventory exceeds 500 units)
        if inventory > 500:
            print("Current inventory: ", inventory)
            print("WARNING:Inventory limit reached. Cannot add more stock.")
            break

        
        

#Function call to start the auditor program
auditor()
