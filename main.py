MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink, resources_in_machine):
    #1
    # result = False
    # for resource in resources_in_machine:
    #     if resource not in MENU[user_input]["ingredients"]: continue
    #     if MENU[user_input]["ingredients"][resource] > resources_in_machine[resource]:
    #         result =  f"no enough {resource} in machine"
    #     else:
    #         result =  True
    # return result

    # #2
    ingredients = MENU[drink]["ingredients"]

    for resource in ingredients:
        needed = ingredients[resource]

        if resources_in_machine[resource] < needed:
             print(f"no enough {resource} in machine")
             return False

    return True

    # #3
    #     for ingredient, amount in MENU[user_input]["ingredients"].items():
    #         if resources_in_machine[ingredient] < amount:
    #             print(f"no enough {ingredient} in machine")
    #             return False
    #     return True



def collect_coins():
    print("Please insert coins.")
    coins = {}

    for coin in COINS:
        coins[coin] = int(input(f"How many {coin}?: "))

    return coins

def check_money(drink,coins):
        total = 0

        for coin, count in coins.items():
            total += count * COINS[coin]

        if total < MENU[drink]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False

        if total > MENU[drink]["cost"]:
            change = total - MENU[drink]["cost"]
            upgrade_change = round(change,2)
            print(f"here is your ${upgrade_change} change")

        return True

def minus_resources(drink,resources_in_machine):
    ingredients = MENU[drink]["ingredients"]

    for resource in ingredients:
        needed = ingredients[resource]

        resources_in_machine[resource] -= needed




def off_process():
    return False

process = True

while process:
    answer = input("What would you like?(espresso, latte, cappuccino): ")


    if answer == "off":
       process = off_process()

    if answer == "report":
        print(f"Water {resources["water"]}ml")
        print(f"milk {resources["milk"]}ml")
        print(f"coffee {resources["coffee"]}g")
        print(f"money ${money}")

    if answer in MENU:
       if check_resources(answer, resources):
            coins = collect_coins()
            if check_money(answer, coins):
                minus_resources(answer,resources)
                print(f"Here is your {answer} ☕ Enjoy!")










