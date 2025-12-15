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
    if MENU[user_input]["ingredients"]["water"] < resources_in_machine["water"]:
        if MENU[user_input]["ingredients"]["coffee"] < resources_in_machine["coffee"]:
            if MENU[user_input]["ingredients"]["milk"] < resources_in_machine["milk"]:
                return "we can do this"
            else:
                return "no enough milk in machine"
        else:
            return  "no enough coffee in machine"
    else:
        return "no enough water in machine"

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
        check_resources(answer, resources)





