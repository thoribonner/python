from data import MENU, resources

profit = 0

def print_report():
    """Prints available resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def sufficient_resources(ingredients):
    """Accepts beverage ingredients. Returns True if all resources available. Returns False if not enough resources."""
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry for the inconvenience, but there is not enough {ingredient}")
            return False
    return True

# def replenish_resources(ingredient)

def process_coins():
    """Returns total calculated from inserted coins."""
    print("Please enter coins.")
    total = float(input("How many quarters? ")) * .25
    total += float(input("How many dimes? ")) * .1
    total += float(input("How many nickels? ")) * .05
    total += float(input("How many pennies? ")) * .01
    return total

def transaction_successful(received, cost):
    """Returns True if transaction succesful. Returns False if transaction unsuccessful."""
    if received >= cost:
        change = round(received - cost, 2)
        global profit
        profit += cost
        if change > 0:
            print(f"Here is your change: {change}")
        return True
    else:
        print(f"Sorry that is not enough money.\nMoney refunded: ${received}.\nBeverage cost: ${cost}")
        return False

def update_resources(ingredients):
    """Accepts beverage ingredients. Updates available resources."""
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

def coffee_machine():
    is_on = True
    while is_on:
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if command == "off":
            is_on = False
        elif command == "report":
            print_report()
        else:
            beverage = MENU[command]
            if sufficient_resources(beverage["ingredients"]):
                payment = process_coins()
                if transaction_successful(payment, beverage["cost"]):
                    update_resources(beverage["ingredients"])
                    print(f"Here is your {command}. ☕️ Enjoy!")

coffee_machine()