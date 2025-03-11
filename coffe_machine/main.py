from data import MENU, resources

def is_resource_sufficient(f_user_choice):
    for i in MENU[f_user_choice]["ingredients"]:
        if MENU[f_user_choice]["ingredients"][i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return True
        return False
def report():
        water_resource = resources["water"]
        milk_resource = resources["milk"]
        coffee_resource = resources["coffee"]
        return (f'''
    Water:{water_resource} ml
    Milk:{milk_resource} ml
    Coffe:{coffee_resource} g
    Money:{money_in_the_machine} $
    ''')

def penny_calculator():
    print("Please insert coins.")
    f_quarters = int(input("How many quarters?"))
    f_dimes = int(input("How many dimes? "))
    f_nickles = int(input("How many nickles? "))
    f_pennies = int(input("How many pennies? "))
    f_money = 0.25 * f_quarters + 0.10 * f_dimes + 0.05 * f_nickles + 0.01 * f_pennies
    return f_money

def check_if_milk_is_needed(user):
    try:
        f_milk = MENU[user]["ingredients"]["milk"]
    except KeyError:
        f_milk = 0
    return f_milk

def resource_deduction(f_user_choice):
    for i in MENU[f_user_choice]["ingredients"]:
        resources[i] -= MENU[f_user_choice]["ingredients"][i]

money_in_the_machine = 0

machine = True

while machine:
    coffee_making = True
    user_choice = input("What would you like? (espresso/latte/cappuccino)" )
    if user_choice == "off":
        machine = False
    if user_choice == "report":
        print(report())
        coffee_making = False
    while coffee_making:

        # water = MENU[user_choice]["ingredients"]["water"]
        # coffee = MENU[user_choice]["ingredients"]["coffee"]
        # milk = check_if_milk_is_needed(user_choice)
        cost = MENU[user_choice]["cost"]
        if is_resource_sufficient(user_choice):
            break
        else:
            pass
        money = penny_calculator()
        if money >= cost:
            change = money - cost
            profit = money - change
            money_in_the_machine += profit
            resource_deduction(user_choice)
            print(f"Here is {round(change,2)}$ in change")
            print(f"Here is your {user_choice}")
            coffee_making = False
        else:
            print("Sorry that is not enough money. Money refunded")
            coffee_making = False




