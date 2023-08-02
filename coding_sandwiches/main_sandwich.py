"""Sandwiches ordering program"""


def phone_integer(m):
    # doc - typing
    """validating that the phone number is only integers

    :param m: string (message)
    :return: integer (multiple - my_phone)
    """
    # validating for an integer for the phone number input
    my_phone = 0
    get_result = True
    while get_result:
        my_phone = input(m)
        if not my_phone.isdigit():
            print("Please enter only numbers")
            continue
        elif len(my_phone) < 6 or len(my_phone) > 12:
            print("Phone should be between 6 and 12 digits")
            continue

        get_result = False
    return my_phone

def get_integer(m, lower, upper):
    # doc - typing
    """validating the integer inputs when choosing from indexes

    :param m: string (message)
    :param lower: integer (smallest index (0))
    :param upper: integer (largest index (len))
    :return: integer
    """
    # validating integer inputs that have a specific range e.g for when I ask the customer to input an index number from an options list
    num = 0
    getting_integer = True
    while getting_integer is True:
        try:
            num = int(input(m))
        except ValueError:
            print("Not an integer")
            continue

        if num < lower:
            # validating if the number the user has entered is too low (below the minimum)
            print("Your value is too low")
        elif num > upper:
            # validating if the number the user has entered is too high (above maximum)
            print("Your value is too high")
        else:
            getting_integer = False
    return num

def get_string(m):
    getting_string = True
    while getting_string is True:
        my_string = input(m)
        if my_string.isalpha():
            getting_string = False
        else:
            print("Please enter only letters")
    return my_string



def confirmation(m, chars = ['Y','N'] ):
    # doc - typing
    """Get specified character input.

    :param m: string (message)
    :param chars: list (allowed characters)
    :return: string (1 character)
    """
    while True:
        # to ask the user if they are sure they want to do this action
        choice = input(m).upper()
        if choice not in chars:
            print("Please enter {}".format(' or '.join(chars)))
        else:
            return choice



def print_menu(M):
    # doc - typing
    """
    :param M: list (menu)
    :return: none
    """
    # printing the sandwich menu
    print("-" * 80)
    for i in range(0, len(M)):
        # formatting the sandwich menu
        output = "{}: {:<40} ${:.2f}".format(i,M[i][0], M[i][1])
        print(output)
    print("-" * 80)
    return None

def order(O,M, lower, upper):
    # doc - typing
    """order function
    :param O: list (my_order)
    :param M: list (menu)
    :param lower: integer (lowest index)
    :param upper: integer (highest index)
    :return: None
    """

    # asking user for integer inputs that correlate to the sandwich index numbers
    print_menu(M)
    m = "Please enter the number of the sandwich you would like: -> "
    index_num = get_integer(m, lower, upper)
    sand_num = get_integer("Please enter how many of this sandwich you would like (limit of 5 sandwiches): -> ", 0, 5)
    output = "You have ordered the {} of the {}".format(sand_num,M[index_num][0])
    print(output)
    # adding the information above into a temporary list, to insert this information into the master list
    temp = [M[index_num][0], M[index_num][1], sand_num]
    O.insert(0, temp)
    return None


def review(O,C):
    # doc - typing
    """reviewing the customer's whole order
    :param O: list (my_order)
    :param C: list (string and integer mixed) - (customer_details)
    :return: None
    """
    # function that allows the user to review their order
    # setting the total to 0 so the total amount due is added onto the total everytime
    total = 0
    print("-" * 80)
    for i in range(0, len(O)):
        sub_total = O[i][2]*O[i][1]
        total += sub_total
        # formatting how the review is printed out
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
    return None





def edit_order(O, lower, upper):
    # doc - typing
    """editing the former order
    :param O: list (my_order)
    :param lower: integer (lowest index)
    :param upper: integer (highest index)
    :return: None
    """
    # function that allows the user to edit their order
    print("-" * 80)
    for i in range(0, len(O)):
        # formatting what they have ordered so far
        output = "{}: {:<40} x{}".format(i, O[i][0], O[i][2])
        print(output)
    print("-" * 80)
    # asking for what sandwich they'd like to edit
    m = "Please enter the index number to update the amount of this sandwich/extra you would like: -> "
    my_index = get_integer(m, lower, upper)
    print("* To remove a sandwich/extra completely, you can enter 0 for the next question")
    # asking user the new amount they would like
    new_amount = get_integer("Enter the new number of this item you would like: -> ", 0, 5)
    old_amount = O[my_index][2]
    O[my_index][2] = new_amount
    # confirming/ letting the user know what has been replaced - the new changes
    output_message = "{} has now been changed to {}.".format(old_amount, new_amount)
    print(output_message)
    if new_amount == 0:
        sandwich_name = O[my_index][0]
        O.pop(my_index)
        delete_message = "{} has been removed from your order". format(sandwich_name)
        print(delete_message)
        return None


def details(O, C):
    # doc - typing
    """gathering the data inputs of the customer details to print on receipt
    :param O: list (my_order)
    :param C: list ((string and integers) - (customer_details)
    :return: None and character (1 - "P" or "D")
    """
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

    # asking the customer to input their details
    name = get_string("Please enter your name: --> ")
    m = "Please enter your phone number: --> "
    phone_number = phone_integer(m)
    # adding these inputs into the customer_details list so it can be kept and printed out in the review function
    C.append(name)
    C.append(phone_number)
    message = "Enter 'P' to pick up your order, to get your order delivered enter 'D': -> "
    deliver = confirmation(message, ["P","D"])
    # checking if they would like pick up or delivery
    if deliver == "P":
        message = "Pick up is free, we'll see you in store later"
        print(message)
        # ask for customer name and phone number
        output = "Here are your details - Name: {},   Phone number: {}".format(name, phone_number)
        print(output)
        return None
    # if they chose delivery then it also asks the user to enter their address and automatically adds $3 to their order total
    elif deliver == "D":
        # showing the user the $3 has been added to their order
        d_message = "Delivery is an extra $3 charge, this will automatically be added to your order total"
        # ask for address
        print(d_message)
        O.append(["Delivery", 3, 1])
        address = input("Please enter an address for delivery: --> ")
        C.append(address)
        # confirming/ letting the user know what their details are that have been recorded
        output = "Here are your details - Name: {},   Phone number: {},   Address: {}". format(name, phone_number, address)
        print(output)
    else:
        return deliver

def extras(E):
    # doc - typing
    """
    :param E: list (extras)
    :return: None
    """
    # printing the sandwich menu
    print("-" * 80)
    for i in range(0, len(E)):
        # formatting the sandwich menu
        output = "{}: {:<40} ${:.2f}".format(i, E[i][0], E[i][1])
        print(output)
    print("-" * 80)
    return None
def add(E, O, lower, upper):
    extras(E)
    a = "Please enter the number of the extra you would like: -> "
    index_num = get_integer(a, lower, upper)
    num = get_integer("Please enter how many servings of this extra you would like (limit is 5: -> ", 0,5)
    output = "You have added {} of {} to your sandwich".format(num, E[index_num][0])
    print(output)
    # adding the information above into a temporary list, to insert this information into the master list
    temp = [E[index_num][0], E[index_num][1], num]
    O.insert(0, temp)



def confirm_order(O,C):
    # doc - typing
    """confirming the order so the next user can start a new one (clears all lists from previously asked inputs)
    :param O: list (my_order)
    :param C: list (string and integers) - (customer_details)
    :return: None
    """
    # basically printing a full receipt
    review(O,C)
    message = "Would you like the confirm your order (Y/N)? --> "
    confirm = confirmation(message)
    if confirm == "Y":
        print("Your order has been confirmed, thank you for being a customer at Marsden's Gourmet Sandwich Bar. ")
        # clearing next lists so that the next time the option menu shows it's starting a new order
        O.clear()
        C.clear()
    elif confirm == "N":
        return None

def input_action():
    # doc -typing
    """
    :return: character (options on menu)
    """
    # getting the user input as to what they would like to do
    my_input = get_string("Please choose an option: -> ").upper()
    return my_input


def main():
    """
    :return: None
    """
    # name , price , quantity
    my_order = []

    # Name, phone number, address
    customer_details = []

    # sandwiches list lives here
    my_list = [
        ["Halloumi Sandwich", 16],
        ["Pork Banh Mi", 19],
        ["Roasted Beetroot Sandwich", 14],
        ["Sausage and Egg Sandwich", 15.5],
        ["Smoked Salmon Deluxe", 16],
        ["Buttermilk Chicken Sandwich", 19],
        ["'Lucky Beef' Steak Sandwich", 19.5],
        ["Milanese and Gremolata Panini", 17],
        ["Snapper Sandwich", 20],
        ["Jalapeño and Cheddar Sandwich", 15]
    ]

    extras = [
        ["Cheese", 1.5],
        ["Bacon", 3],
        ["Avocado", 2],
        ["Salsa", 2],
        ["Lettuce", 1.5],
        ["Tomato", 1.5],
        ["Cucumber", 1],
        ["Grilled Chicken", 5]
    ]

    # options menu
    my_menu = ['P : Print menu',
               'O : Order',
               'A : Add extras',
               'E : Edit order',
               'D : Details',
               'R : Review',
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
            order(my_order, my_list, 0, len(my_list)-1)
        elif user_choice == "R":
            review(my_order, customer_details)
        elif user_choice == "E":
            edit_order(my_order, 0, len(my_order)-1)
        elif user_choice == "D":
            details(my_order, customer_details)
        elif user_choice == "C":
            confirm_order(my_order, customer_details)
        elif user_choice == "A":
            add(extras, my_order, 0, len(extras)-1)
        elif user_choice == "Q":
            run = False
            print("Thank you for visiting Marsden's Gourmet Sandwich Bar")
        else:
            print("Unrecognised entry, this is not an option")
    return None

main()
