"""Sandwiches ordering program"""

def get_integer(m):
    get_result = True
    while get_result:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("you have not entered an integer")
            continue
        get_result = False
    return my_integer

def get_string(m):
    my_string = input(m).upper()
    return my_string



def confirmation(m, chars=['Y','N'] ):
    """Get specified character input.

    :param m: string (message)
    :param chars: list (allowed characters)
    :return: string (1 character)
    """
    while True:
        choice = input(m).upper()
        if choice not in chars:
            print( "Please enter {}".format(' or '.join(chars) ) )
        else:
            return choice


def print_menu(M):
    print("-" * 80)
    for i in range(0, len(M)):
        output = "{}: {:<40} ${:.2f}".format(i,M[i][0], M[i][1])
        print(output)
    print("-" * 80)
    return None

def order(O,M):
    print_menu(M)
    index_num = get_integer("Please enter the number of the sandwich you would like: -> ")
    sand_num = get_integer("Please enter how many of this sandwich you would like: -> ")
    output = "You have ordered the {} of the {}".format(sand_num,M[index_num][0])
    print(output)
    temp = [M[index_num][0], M[index_num][1], sand_num]
    O.insert(0, temp)


def review(O,C):
    total = 0
    print("-" * 80)
    for i in range(0, len(O)):
        sub_total = O[i][2]*O[i][1]
        total += sub_total
        order_item = "x{:<5} {:<40} @ ${:5.2f} each = ${:5.2f} ".format(O[i][2], O[i][0], O[i][1], sub_total)
        print(order_item)

    output = "{:>64}${:5.2f}".format("Total = ", total)
    print("-" * 80)
    print(output)
    print("-" * 80)
    print("Customer details")
    # print customer details
    if len(C) == 0:
        message = "You have not yet entered any customer details"
        print(message)
    else:
        last_item = O[-1]
        if last_item[0] == "Delivery":
            customer_details = "Delivery for - Name: {}, Phone Number: {}, Address: {}".format(C[0], C[1], C[2])
            print(customer_details)
        elif last_item[0] != "Delivery":
            details = "Pick up for - Name: {}, Phone Number: {} ".format(C[0], C[1])
            print(details)
    print("-" * 80)





def edit_order(O):
    print("-" * 80)
    for i in range(0, len(O)):
        output = "{}: {:<40} x{}".format(i, O[i][0], O[i][2])
        print(output)
    print("-" * 80)
    my_index = get_integer("Please enter the index number to update the amount of this sandwich you would like: -> ")
    new_amount = get_integer("Enter the new number of this sandwich you would like: -> ")
    old_amount = O[my_index][2]
    O[my_index][2] = new_amount
    output_message = "{} has now been changed to {}.".format(old_amount, new_amount)
    print(output_message)
    if new_amount == 0:
        sandwich_name = O[my_index][0]
        O.pop(my_index)
        delete_message = "{} has been removed from your order". format(sandwich_name)
        print(delete_message)

def details(O, C):
    # test if details are already there
    if len(C) != 0:
        message = "You have already entered details, do you want to enter them again (Y/N)? --> "
        choice = confirmation(message)
        if choice == "Y":
            C.clear()
            last_item = O[-1]
            if last_item[0] == "Delivery":
                O.pop()
        elif choice == "N":
            return None


    name = input("Please enter your name: --> ")
    phone_number = get_integer("Please enter your phone number: --> ")
    C.append(name)
    C.append(phone_number)
    message = "Enter 'P' to pick up your order, to get your order delivered enter 'D': -> "
    deliver = confirmation(message, ["P","D"])

    if deliver == "P":
        message = "Pick up is free, we'll see you in store later"
        print(message)
        # ask for customer name and phone number
        output = "Here are your details - Name: {},   Phone number: {}".format(name, phone_number)
        print(output)
        return None
    elif deliver == "D":
        # showing the user the $3 has been added to their order
        d_message = "Delivery is an extra $3 charge, this will automatically be added to your order total"
        # ask for address
        print(d_message)
        O.append(["Delivery", 3, 1])
    # get customer details
    # ask for customer name, phone number, address
        address = input("Please enter an address for delivery: --> ")
        C.append(address)
        output = "Here are your details - Name: {},   Phone number: {},   Address: {}". format(name, phone_number, address)
        print(output)
    else:
        return deliver


def confirm_order(O,C):
    review(O,C)
    confirm = get_string("Would you like the confirm your order (Y/N)? --> ")
    if confirm == "Y":
        print("Your order has been confirmed, thank you for being a customer at Marsden's Gourmet Sandwich Bar. ")
        # clearing next lists so that the next time the option menu shows it's starting a new order
        O.clear()
        C.clear()
    elif confirm == "N":
        return None

def input_action():
    my_input = get_string("Please choose an option: -> ")
    return my_input



def main():
    my_order = []
    my_order = [
        # name , price , quantity
        ["Roasted Beetroot Sandwich", 14, 3],
        ["Jalapeño and Cheddar Sandwich", 15, 7],
    ]
    # Name, phone number, address
    customer_details = []

    # sandwiches list lives here

    my_list = [
        ["Halloumi Sandwich", 16],
        ["Pork Banh Mi", 19],
        ["Roasted Beetroot Sandwich", 14],
        ["Sausage and Egg Sandwich", 15.5],
        ["Smoked Salmon Deluxe", 16],
        ["Ham Sandwich", 14],
        ["Buttermilk Chicken Sandwich", 19],
        ["'Lucky Beef' Steak Sandwich", 19.5],
        ["Milanese and Gremolata Panini", 17],
        ["Snapper Sandwich", 20],
        ["Jalapeño and Cheddar Sandwich", 15]
    ]


    my_menu=['P : Print menu',
             'O : Order',
             'R : Review',
             'E : Edit order',
             'D : Details',
             'C : Confirm order',
             'Q : Quit'
             ]

    run = True
    new_order = True
    while run is True:
        if new_order is True:
            print("Starting new order")
            new_order = False
        print("-" * 80)
        for m in my_menu:
            print(m)
        user_choice = input_action()
        if user_choice == "P":
            print_menu(my_list)
        elif user_choice == "O":
            order(my_order, my_list)
        elif user_choice == "R":
            review(my_order, customer_details)
        elif user_choice == "E":
            edit_order(my_order)
        elif user_choice == "D":
            details(my_order, customer_details)
        elif user_choice == "C":
            confirm_order(my_order, customer_details)
        elif user_choice == "Q":
            run = False
            print("Thank you for visiting Marsden's Gourmet Sandwich Bar")
        else:
            print("Unrecognised entry, this is not an option")

main()
