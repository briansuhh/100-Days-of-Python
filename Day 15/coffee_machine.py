MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def subtract_resources(drink):
    """Return False if resources are not enough; otherwise, return True"""
    for ingredients, amount in MENU[drink]["ingredients"].items():
        if amount > resources[ingredients]:
            return False
    for ingredients, amount in MENU[drink]["ingredients"].items():
        resources[ingredients] -= amount
    return True
        

def change(payment, drink_cost):
    """Refund the payment if the money is to be refunded; otherwise, return the change of payment."""
    if payment < drink_cost:
        return payment
    return payment - drink_cost

    
machine_money = 0
while 1:
    user_input = input("  What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        exit()

    if user_input == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        print(f"Money: {machine_money}")
        continue

    if user_input not in MENU:
        print("Please select something from the MENU.")
        continue

    if not subtract_resources(user_input):
        print(f"Sorry, not enough water to make {user_input}")
    else:
        drink = MENU[user_input]
        print(f"The {user_input} costs ${drink['cost']}")
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total_payment = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        change_amount = change(total_payment, drink["cost"])

        if change_amount == total_payment:
            print(f"Sorry {total_payment} is not enough to buy a {user_input}. Money refunded.")
        else:
            machine_money += drink["cost"]
            print(f"Here is your change: ${change_amount:.2f}")
            print(f"Here is your {user_input}. Enjoy!")