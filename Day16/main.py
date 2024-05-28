from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from moneymachine import MoneyMachine

# Create MenuItem objects
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

# Create a Menu and add the drinks
menu = Menu()
menu.add_menu_item(espresso)
menu.add_menu_item(latte)
menu.add_menu_item(cappuccino)

# Create CoffeeMaker and MoneyMachine objects
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    choice = input(f"What would you like? Choose between espresso, latte or cappuccino: ").lower()
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
