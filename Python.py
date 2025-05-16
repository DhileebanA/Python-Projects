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


def change(p, n, d, q):
    m = p * 0.01 + n * 0.05 + d * 0.10 + q * 0.25
    bal = round(m - MENU[user_choose]["cost"], 2)
    global money, resources
    if m < MENU[user_choose]["cost"]:
        print(f"Sorry that's not enough money. Money refunded ${m}")
    elif bal == 0:
        money = +MENU[user_choose]["cost"]
        print(f"Here is your {user_choose} ☕")
        resources.update(new)
    else:
        money = +MENU[user_choose]["cost"]
        print(f"Here is your change ${bal}")
        print(f"Here is your {user_choose} ☕")
        resources.update(new)


def check_resource():
    for item in MENU[user_choose]["ingredients"]:
        if resources[item] < MENU[user_choose]["ingredients"][item]:
            global res
            res = False
            print(f"Sorry there is not enough {item}")
            return
        else:
            new[item] = resources[item] - MENU[user_choose]["ingredients"][item]


on = True
new = {}
money = 0

while on:
    user_choose = input("What would you like?(espresso/latte/cappuccino): ").lower()
    res = True
    if user_choose == "off":
        on = False
        break
    elif user_choose == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f"Money: ${money}")
    elif user_choose == 'espresso' or user_choose == 'latte' or user_choose == 'cappuccino':
        check_resource()
        if res:
            print("\nPlease insert number of coins.")
            pe = float(input("Insert penny: "))
            ni = float(input("Insert nickel: "))
            di = float(input("Insert dime: "))
            qu = float(input("Insert quarter: "))
            change(pe, ni, di, qu)

    else:
        print('\nCheck your spelling. Make sure you entered valid input.'
              '\n(or)\n"report" for remaining resource. "off" for close')
    print(new)
