class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

drinks = {
    "Mojito": Drink("Mojito", 8.99),
    "Old Fashioned": Drink("Old Fashioned", 9.99),
    "Martini": Drink("Martini", 7.99),
    "Gin Tonic": Drink("Gin Tonic", 6.99),
    "Cosmopolitan": Drink("Cosmopolitan", 8.49),
    "Whiskey Sour": Drink("Whiskey Sour", 7.49)
}

def display_menu():
    print("\n            Menu:\n")
    counter = 1
    for drink in drinks.values():
        print(f"{counter}. {drink}")
        counter += 1

display_menu()

ordered_drinks = [] # a list to store the ordered drinks

while True:
    order = input("\nWhat would you like to order? (To exit type 'q') ")

    if order.lower() == "q":
        print("\nThank you for visiting Dry Martini. Cheers!\n")
        break

    if order.title() in drinks:
        drink = drinks[order.title()]
        print(f"\nYou ordered a {drink}. Cheers!\n")
        ordered_drinks.append(drink) # add the drink to the list
    elif order.isdigit() and int(order) in range(1, len(drinks) + 1):
        drink = list(drinks.values())[int(order) - 1]
        print(f"\nYou ordered a {drink}. Cheers!\n")
        ordered_drinks.append(drink) # add the drink to the list
    else:
        print("Sorry, we don't have that drink in our menu. Please try again.")
    
    display_menu()

# calculate the total price of the ordered drinks
total_price = 0
for drink in ordered_drinks:
    total_price += drink.price

# ask the user for the total price
print(f"\nThe total price of your order is ${total_price:.2f}. Would you like to pay now? (y/n) ")
answer = input()
if answer.lower() == "y":
    print("\nThank you for your payment. Have a nice day!\n")
else:
    print("\nPlease pay before you leave. Thank you!\n")
    