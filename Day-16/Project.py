from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    m = menu.get_items()
    choice = input(f"What do you want to order? {m}")
    if choice == "off":
        break
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink =  menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)