def confirmation(m):
    while True:
        choice = input(m).upper()
        if choice not in ['Y','N']:
            print("Please enter Y or N")
        else:
            return choice



m= "You have already chosen delivery do you want to change? (Y/N): -- >"
result = confirmation(m)
print(result)
