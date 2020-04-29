def myFunc():
    num_1 = int(input("Please enter your first number: "))
    num_2 = int(input("Please enter your second number: "))
    print(num_1+num_2)
    

is_Running = True

while is_Running == True: 

    try: 
        myFunc()
    except ValueError:
        print('I said enter a number...')

    choice = input('Contine or press "q" to quit ')

    if choice == 'q':
        break 
