def confirmation(m):
    while True:
        choice = input(m).upper()
        if choice not in ['Y','N']:
            print("Please enter Y or N")
        else:
            return choice



m= "You have already chosen delivery do you want to change? (Y/N): -- >"
#result = confirmation(m)
#print(result)

def confirmation(m, chars=['Y','N'] ):
    while True:
        choice = input(m).upper()
        if choice not in chars:
            print( "Please enter {}".format(' or '.join(chars) ) )
        else:
            return choice


def get_integer(m, lower, upper):
    num = 0
    getting_integer = True
    while getting_integer is True:
        try:
            num = int(input(m))
        except ValueError:
            print("Not an integer")
            continue

        if num < lower:
            print("You value is too low")
        elif num > upper:
            print("You value is too high")
        else:
            getting_integer = False
    return num


m="Please enter number: "
my_list = ["a","b", "c"]
num=get_integer(m, 0, len(my_list)-1)

print(my_list[num])

