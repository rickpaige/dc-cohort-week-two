def name(user_name):
   with open("guest.txt", "w") as file:
     file.write(user_name)

def programming(user_input):
    with open("programming.txt", "a") as file: 
        file.write(user_input)
        file.write("\n")

def response(programming):
    with open("programming.txt") as file:
        programming = file.readprogramming()
        print(programming)

def line_thing():
    print("<-------------------------------------->")

is_Running = True

user_name = input('What is your name? ')
name(user_name)
line_thing()


while is_Running:
    print(f'Hello {user_name}! Type "talk" to tell me why you enjoy programming? ')
    line_thing()
    print('To see your answers, type "list" into the console.' )
    line_thing()
    print('Press q to quit! ')
    line_thing()
    
    choice = input("What would you like to do? ")
    line_thing()

    if choice == 'q':
        is_Running = False

    elif choice == 'talk':
        user_input = input(f'Why do you like programming {user_name}? ')
        programming(user_input)
        line_thing()
    
    elif choice == 'list':
        print(f'Why {user_name} likes to program: ')
        response(programming)

        

   
    
    
