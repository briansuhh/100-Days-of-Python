from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

while 1:
    user_input = input(f"   What drink do you want? {menu.get_items()} ")
    
    if user_input == 'off':
        exit()
    elif user_input == 'report':
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(user_input)

        if drink == None:
            continue

        if moneymachine.make_payment(drink.cost) and coffeemaker.is_resource_sufficient(drink):
            coffeemaker.make_coffee(drink)