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
    my_string = input(m)
    return my_string

def order(O,M):
    print("-" * 80)
    print_menu(M)
    print("-" * 80)
    index_num = get_integer("Please enter the number of the sandwich you would like: -> ")
    sand_num = get_integer("Please enter how many of this sandwich you would like: -> ")
    output = "You have ordered the {} of the {}".format(sand_num,M[index_num][0])
    print(output)
    temp = [M[index_num][0], M[index_num][1], sand_num]
    O.append(temp)


def review(O):
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

def transport(O):
    deliver = get_string("Enter 'P' to pick up your order, to get your order delivered enter 'D': -> ")
    if deliver == "P":
        message = "Pick up is free, we'll see you in store later"
        print(message)
    elif deliver == "D":
        d_message = "Delivery is an extra $3 charge, this will automatically be added to your order total"
        print(d_message)
        total = 0
        print("-" * 80)
        for i in range(0, len(O)):
            sub_total = O[i][2] * O[i][1]
            total += sub_total
            order_item = "x{:<5} {:<40} @ ${:5.2f} each = ${:5.2f} ".format(O[i][2], O[i][0], O[i][1], sub_total)
            delivery = "{:>64}$3.00". format("Delivery Fee = ")
            print(order_item)
        print(delivery)
        output = "{:>64}${:5.2f}".format("Total = ", total + 3)
        print("-" * 80)
        print(output)
        print("-" * 80)


def input_action():
    my_input = input("Please choose an option: -> ").upper()
    return my_input


def print_menu(M):
    for i in range(0, len(M)):
        output = "{}: {:<40} ${:.2f}".format(i,M[i][0], M[i][1])
        print(output)
    return None

def main():
    my_order = []
    my_order = [
        # name , price , quantity
        ["Roasted Beetroot Sandwich", 14, 3],
        ["Jalapeño and Cheddar Sandwich", 15, 7]
    ]
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
             'T : Pick up or delivery',
             'Q : Quit'
             ]

    run = True
    while run is True:
        for m in my_menu:
            print(m)
        user_choice = input_action()
        if user_choice == "P":
            print_menu(my_list)
        elif user_choice == "O":
            order(my_order, my_list)
        elif user_choice == "R":
            review(my_order)
        elif user_choice == "E":
            edit_order(my_order)
        elif user_choice == "T":
            transport(my_order)
        elif user_choice == "Q":
            run = False
            print("Thank you for visiting Marsden Gourmet Sandwich Bar")
        else:
            print("Unrecognised entry, this is not an option")

main()