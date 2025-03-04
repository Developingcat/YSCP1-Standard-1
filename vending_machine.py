# vending_machine.py

# Display menu
def display_menu():
    print("\n********************************************************")
    print("***                                                  ***")
    print("***      Welcome to the Python Vending Machine!      ***")
    print("***                                                  ***")
    print("********************************************************\n")

    print("1. Soda - $1.25")
    print("2. Chips - $1.00")
    print("3. Candy - $0.75")
    print("Enter 'q' to quit.")
    print("******************\n")



# Calculate change
def calculate_change(payment, cost):
    return payment - cost  # It was subtracting 0.10 cents from the final 

# Operate Vending Machine
def vending_machine():
    items = {"1": 1.25, "2": 1.00, "3": 00.75} # The third option was forgotten here 
    while True:
        display_menu
        choice = input("\nSelect an item (1-3) or 'q' to quit: ")

        if choice == 'q':
            print("\nThank you for using the vending machine!\n")
            break

        if choice not in items:
            print("\nInvalid selection. Please choose again.\n") # Works good!! 
            continue

        try:
            payment = float(input(f"\nEnter payment for item (${items[choice]:.2f}): "))
            if payment < items[choice]:
                print("\nInsufficient payment. Transaction canceled.")
                continue
            change = calculate_change(payment, items[choice])
            print(f"\nYour change is ${change:.2f}. Enjoy your snack!\n\n") 
        except ValueError:  # Handle non-numeric input
            print("\nInvalid input. Please enter a numeric value.\n") # Also works good!! 


if __name__ == "__main__":
    vending_machine()
