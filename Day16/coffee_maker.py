from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from moneymachine import MoneyMachine

# Initialize the Menu, CoffeeMaker, and MoneyMachine objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    # Display the available options to the user
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    
    if choice == 'off':
        print("Have a good one!")
        on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print("Sorry, that item is not available.")
