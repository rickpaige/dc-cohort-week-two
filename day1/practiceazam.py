class Book: 
    def __init__(self): 
        # properties 
        self.title = ""
        self.author = ""
        self.price = ""
        self.isbn = ""




book = Book() 
book.title = "Lord of the Rings"
book.isbn = "333"

book2 = Book() 
book.title = "Harry Potter"
book.isbn = "33344"

class Table: 
    def __init__(self, width, height): 
        self.width = width
        self.height = height
        self.serial_number = "123"
        self.material = ""

table = Table(100, 200)


# create an instance/object of the Table class to create specific table 



class User: 
    def __init__(self, username, password): 
        self.username = username
        self.password = password 

user = User("johndoe", "password") 



# Creating a Class 

class Car: 
    def __init__(self, make, model): # initializer/constructor 
        # define properties of the car 
        self.make = make 
        self.model = model 
        self.color = "White" 
        self.vin = ""


car2 = Car("Toyota", "Camry")
car2.color = "Black"
car2.vin = "123"


car = Car() # creating an object/instance of Car class 
car.make = "Honda"
car.model = "Accord"
car.vin = "123"
car.color = "Green"




car2 = Car() 




 



