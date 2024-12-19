# Simple Food Ordering System

def display_menu():
    menu = {
        'Pork Sinigang': 130.00,
        'Chicken Adobo': 120.00,
        'Dinuguan': 80.00,
        'Pinakbet': 90.00
    }
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: Php {price:.2f}")
    return menu

def select_order(menu):
    while True:
        choice = input("\nEnter the ulam you want to order: ").title()
        if choice in menu:
            print(f"You selected {choice}. Price: Php {menu[choice]:.2f}")
            return choice, menu[choice]
        else:
            print("Invalid choice. Please select an ulam only from the menu.")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input(f"\nYour total is Php {total_cost:.2f}. Enter cash amount: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment accepted. Your change is Php {change:.2f}.")
                break
            else:
                print("Insufficient amount. Please provide enough cash to cover the total cost.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Angel's Karinderya!")
    menu = display_menu()
    item, price = select_order(menu)
    process_payment(price)
    print("\nThank you for your order! Have a great day!")

if __name__ == "__main__":
    main()
