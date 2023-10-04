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
    "Money":0
}

def coffeemaker(resources,coffe,total):
    if coffe == 'cappuccino' or coffe == 'latte':
        moneycost = MENU[coffee]["cost"]  
        watercost = MENU[coffee]["ingredients"]["water"]      
        milkcost = MENU[coffee]["ingredients"]["milk"]  
        coffeecost = MENU[coffee]["ingredients"]["coffee"] 
    elif coffe == 'espresso':
        moneycost = MENU[coffee]["cost"]  
        watercost = MENU[coffee]["ingredients"]["water"]
        coffeecost = MENU[coffee]["ingredients"]["coffee"] 
    if total > moneycost and coffe == 'cappuccino':
        resources["Money"] += moneycost
        resources["water"] -= watercost
        resources["milk"] -= milkcost
        resources["coffee"] -= coffeecost
        total -= moneycost
        print(f"Your change is {total:.2f}")  
    elif total > moneycost and coffe == 'latte':
        resources["Money"] += moneycost
        resources["water"] -= watercost
        resources["milk"] -= milkcost
        resources["coffee"] -= coffeecost
        total -= moneycost
        print(f"Your change is {total:.2f}")                       
    elif total > moneycost and coffe == 'espresso':
        resources["Money"] += moneycost
        resources["water"] -= watercost
        resources["coffee"] -= coffeecost
        total -= moneycost
        print(f"Your change is {total:.2f}")
    elif total < moneycost :
        print(f"Sorry This is not enough money")

    
def resources_checker(resources,coffe,pennies,dimes,nickles,quarters):
    total = quarters* 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    
    if coffe == 'cappuccino' or coffe == 'latte':
        if resources["water"] < MENU[coffee]["ingredients"]["water"]:
            print("Water is not available")
            return True
        elif resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Mlik is not available")
            return True
        elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
            print("Coffee is not available")
            return True
        else:
            coffeemaker(resources,coffe,total)
            return True

    elif coffe == 'espresso':
        if resources["water"] < MENU[coffee]["ingredients"]["water"]:
            print("Water is not available")
            return True
        elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
            print("Coffee is not available")
            return True
        else:
            coffeemaker(resources,coffe,total)
            return True
    
        
        
def report(resourcse):
    for key, values in resources.items():
        print(f"{key}: {values}")  

#quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
flag = True
while flag:
    coffee = input("Enter The Name Of Coffee: ")
    if coffee == "latte" or coffee == "cappuccino" or coffee == "espresso":
        quarters = float(input("Enter The quarters "))
        dimes = float(input("Enter The Dimes "))
        nickles = float(input("Enter The Nickles "))
        pennies = float(input("Enter The Pennies "))
        flag = resources_checker(resources,coffee,pennies,dimes,nickles,quarters)
    elif coffee == "Off":
            break
    elif coffee == "report":
        report(resourcse=resources)
