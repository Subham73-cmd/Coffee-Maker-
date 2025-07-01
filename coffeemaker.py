MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 20,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 25,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 30,
        },
        "cost": 3.0,
    }
}

profit = 0  #Initilizing profit to 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def resource_sufficient(ingredients):
    """Returns true if the resources are sufficient or returns false if they are not"""
    for items in ingredients:
        if ingredients[items]>resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True
def count_coins():
    """Returns the total calculation of inserted coins"""
    print("Please insert coins.")
    total=int(input("How many quarters ?: "))*0.25
    total+=int(input("How many dimes ?: "))*0.1
    total+=int(input("How many nickels ?: "))*0.05
    total+=int(input("How many pennies ?: "))*0.01
    return total
def transaction_status(money_received, drink_cost):
    if money_received>drink_cost:
        change=round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money.")
        return False
def prepare_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]   #Deducts the required ingredients from the total resources
    print(f"Here is your {drink_name}, Enjoy.")
is_on=True
while is_on:
    choice=input("What would you like ?(Espresso/Latte/Cappuccino): ")
    if choice=="off":
        is_on=False   #Machine turns off during maintenance
    elif choice=="report":      #Gives a report of the remaining resources
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Profit: {profit}")
    else:
        drink=MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment=count_coins()
            if transaction_status(payment, drink["cost"]):
                prepare_coffee(choice, drink["ingredients"])