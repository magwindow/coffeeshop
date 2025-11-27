import os
import json


def main_menu(orders):
    while True:
        order = get_order()
        if order == {}:
            print("You entered 'X', exiting...")
            return
        print("Check your order:")
        print_order(order)
        confirm = input("Confirm? Press Y to confirm, N to cancel: ")
        if confirm == "Y" or confirm == "y":
            orders.append(order)
            print("Thanks for your order:")
            print_order(order)
        else:
            continue


def menu(choices, title="Erik's Menu", prompt="Choose your item: "):
    print(title)
    print(len(title) * "-")
    for i, c in enumerate(choices, 1):
        print(i, c)
    while True:
        choice = input(prompt)
        allowed_answers = [str(a) for a in range(1, len(choices) + 1)]

        allowed_answers.append("X")
        allowed_answers.append("x")

        if choice in allowed_answers:
            if choice == "X" or choice == "x":
                answer = ""
                break
            else:
                answer = choices[int(choice) - 1]
                break
        else:
            print("Enter number from 1 to ", len(choices))
            answer = ""
    return answer


def read_menu(filename):
    with open(filename) as f:
        temp = f.readlines()
        result = [item.strip() for item in temp]
    return result


def get_order():
    order = {}
    name = input("Enter your name or enter 'X' to exit: ")
    if name == "X" or name == "x":
        return {}
    else:
        order["name"] = name
    drinks = read_menu("drinks.txt")
    flavors = read_menu("flavors.txt")
    toppings = read_menu("toppings.txt")
    order["drink"] = menu(drinks, "Erik's drinks", "Choose your drink: ")
    order["flavor"] = menu(flavors, "Erik's flavors", "Choose your flavor: ")
    order["topping"] = menu(toppings, "Erik's toppings", "Choose your topping: ")
    return order


def print_order(order):
    print("Here is your order, ", order["name"])
    print("Main product: ", order["drink"])
    print("Flavor: ", order["flavor"])
    print("Topping: ", order["topping"])
    print("Thanks for your order!")
    return


def save_orders(orders, filename):
    with open(filename, "w") as f:
        json.dump(orders, f, indent=4)
        return


def load_orders(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            orders = json.load(f)
            return orders
    else:
        orders = []
        return orders


orders = load_orders("orders.json")
main_menu(orders)
save_orders(orders, "orders.json")
