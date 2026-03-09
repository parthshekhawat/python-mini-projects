MENU = {
    "espresso": {"ingredients": {"water": 50,
                                 "milk" : 0,
                                 "coffee": 18},
                 "cost": 1.5,
    },
    "latte": {"ingredients": {"water": 200,
                              "milk": 150,
                              "coffee": 24,},
              "cost": 2.5,
    },
    "cappuccino": {"ingredients": {"water": 250,
                                   "milk": 100,
                                   "coffee": 24,},
                   "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


earning = 0
import os
import time

def check_resources(coffee_choice):
    """checks if resources are sufficient, if not adds them to a list and returns it"""
    out_of_item = []
    for ingredient in coffee_choice:
        if resources[ingredient] < coffee_choice[ingredient]:
            out_of_item.append(ingredient)
    return out_of_item

def get_payment():
    """receives payment and returns user paid amount"""
    user_gave = int(input("How many quarters: "))*0.25
    user_gave += int(input("How many dimes: ")) * 0.10
    user_gave += int(input("How many nickles: "))*0.05
    user_gave += int(input("How many pennies: ")) * 0.01
    return user_gave


def process_transaction(coffee_choice, money, coffee_order):
    """processes remaining transaction"""
    #I expect coffee_choice in the format MENU[order]
    change = money - coffee_choice["cost"] 
    if change < 0:
        print(f"This is not enough money, please add {-change} more and retry ordering.")
        return False
    elif change == 0:
        print(f"You have paid {money}$.")
        print(f"Enjoy your {coffee_order}!")  
        return True
    else:
        print(f"You have paid {money}$.")
        print(f"Here is your change {round(change,2)}, enjoy your {coffee_order}!")  
        return True

def is_another_command(command):
    if command == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(earning)
        return True

    elif command == 'off':
        print("The machine is currently out of service.")
        return False

    elif command not in MENU:
        print("Invalid choice. Try again from espresso, latte, or cappuccino.")
        return True
    return True

working = True
while working:
    order = input("What would you like to order? (espresso/latte/cappuccino): ").strip().lower()

    if order not in MENU:
        working = is_another_command(order)

    else:
        user_drink = MENU[order]
        #check if resources are sufficient, if sufficient go through with the payment.
        is_out_of_item = check_resources(user_drink["ingredients"])
        if is_out_of_item:
            print(f"Sorry, we are out of {is_out_of_item}.")
            working = True

        else:

            money_received = round(get_payment(),2)
            is_transaction_successful = process_transaction(user_drink, money_received, order)

            if is_transaction_successful:
                earning += user_drink["cost"]
                for item in user_drink["ingredients"]:  
                    resources[item] -= user_drink["ingredients"][item]

            time.sleep(2)
            os.system("cls")
            working = True