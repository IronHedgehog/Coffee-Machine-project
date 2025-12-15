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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(user_input, resources_in_machine):
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
    ingredients = MENU[user_input]["ingredients"]

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

def off_process():
    return False

process = True

while process:
    answer = input("What would you like?(espresso, latte, cappuccino): ")
    money = 0

    if answer == "off":
       process = off_process()

    if answer == "report":
        print(f"Water {resources["water"]}ml")
        print(f"milk {resources["milk"]}ml")
        print(f"coffee {resources["coffee"]}g")
        print(f"money ${money}")

    if answer == "espresso":
       print(check_resources(answer, resources))





