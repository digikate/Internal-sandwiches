def print_sandwiches():
    my_list = [
        "Halloumi Sandwich" "$16",
        "Pork Banh Mi" "$19",
        "Roasted Beetroot Sandwich" "$14",
        "Sausage and Egg Sandwich" "$15.5",
        "Smoked Salmon Deluxe" "$16",
        "Ham Sandwich" "$14",
        "Buttermilk Chicken Sandwich" "$19",
        "'Lucky Beef' Steak Sandwich" "$19.5",
        "Milanese and Gremolata Panini" "$17",
        "Snapper Sandwich" "$20",
        "Jalapeño and Cheddar Sandwich" "$15"
    ]

    [print(x) for x in my_list]

def input_action():
    my_input = input("Please choose an option")
    return my_input

def menu():
    my_menu = '''
    A : print menu
    B : quit
    '''
    run = True
    while run is True:
        print(my_menu)
        user_choice = input_action()
        if user_choice == "A":
            print_sandwiches()
        elif user_choice == "B":
            run = False
            print("Thank you for visiting Marsden Gourmet Sandwich Bar")
        else:
            print("Unrecognised entry, this is not an option")
menu()