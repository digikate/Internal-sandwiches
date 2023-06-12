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

def order(O):
        c = get_integer("How many sandwiches would you like to order?")
        i = 0
        while i < c:
            my_order = get_string("Please enter the index number of the sandwich you would like to order:")
            O.append(my_order)
            i += 1
def input_action():
    my_input = input("Please choose an option").upper()
    return my_input


def print_menu(M):
    for i in range(0, len(M)):
        output = "{}: {:<40} ${:.2f}".format(i,M[i][0], M[i][1])
        print(output)
    return None

def main():
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

    my_order = []

    my_menu = '''
    P : Print menu
    O : Order
    Q : Quit
    '''
    run = True
    while run is True:
        print(my_menu)
        user_choice = input_action()
        if user_choice == "P":
            print_menu(my_list)
        elif user_choice == "O":
            order(my_order)
        elif user_choice == "Q":
            run = False
            print("Thank you for visiting Marsden Gourmet Sandwich Bar")
        else:
            print("Unrecognised entry, this is not an option")

main()