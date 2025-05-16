from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
pay = MoneyMachine()
is_on = True

while is_on:
    choose = input(f'What do you like {(menu.get_items())} ').lower()
    drink = menu.find_drink(choose)
    if choose == 'off':
        print('Thankyou')
        is_on = False
    elif choose == 'report':
        coffee.report()
        pay.report()
    else:
        if coffee.is_resource_sufficient(drink) and pay.make_payment(drink.cost):
            coffee.make_coffee(drink)


