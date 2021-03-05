#Mo - App Assinment_1: Seaborn's Bar and Fire Grill 
print()
while True:# Executed until code is satisfied
    try:
        print("Thanks for choosing Seaborn's Bar and Fire Grill")
        print()
        check = float(input("what is the total of your check?\n"))
        print()
        break 
    except ValueError:
        print()
        print("Try typing in a number.")
while True:
    tip_choice = input("Enter a Tip Amount:  'a' for 15%, 'b' for 18%, or 'c' for 20, 'd' for other\n")
    if tip_choice not in('a', 'b', 'c'): #Will allow user to enter a different entry 
        d = float(input('Enter a different Tip amount:,\n'))/100
        total_check = check + (check*d)
        print(f'Your total is ${total_check}.')
    elif tip_choice == "a": #will calculate the total amount
        total_check = (.15 * check) + check
    elif tip_choice == "b":
        total_check = (.18 * check) + check
    elif tip_choice == "c":
        total_check = (.20 * check) + check
    
    split= (input(f"The Total is  ${total_check}, Will you split your check? Enter ('y') for Yes or ('n') for No,\n"))#split check with user input 
    if split == "y":
        num_of_checks= int(input('Enter number of Guests sharing the bill?,\n'))
        total = total_check/num_of_checks
        print('Each Guest wil owe $%.2f' % total, "\n")# (total) printed will be a float containing 2 decimal places 
        (print)
        print("Thanks for dining at Seaborn's!")
    elif split == "n":
        print("Thanks for dining at Seaborn's!")
    break
print()


