# Table:
# --attributes/properties
# -Color
# -Height
# -Width
# -Length
# -Material
# -Shape 
# -Weight 
# -Price

# OfficeTable - Table
# Color = Black 
# Width = 100
# Height = 100 

# table = ['Color': 'Blue', 'Price': 100, 'Material': 'Cherry Wood']


# # Creating a class in python

# Product: 
#  -title
#  -description
#  -price 
#  -imageURL




# class Car: 
#     def __init__(self, make, model): # initializer/constructor
#         # define properties of the car
#         # self represents the object of particular class
#         self.make = make
#         self.model = model
#         color = ""      #properties must have self tag before 
#         self.vin = ""


# car = Car() # creating an object/instance of Car class, can be named whatever
# car.make = "Fiat"
# car.model = "500L"
# car.vin = "1234"
# car.color = n/a # no self.color in Class

# car2 = Car()
# car2.make = "Toyota"
# car2.model = "Camry"


# class Table:
#     def __init__(width, height, material, price):
#         self.width = width
#         self.height = height
#         self.material = material 
#         self.price = price

# table = Table(100, 200, 'Oak', '$50')
# class Car: 
#     def __init__(self, make, model): 
#         self.make = make
#         self.model = model
#         self.drive = ""     
#         self.vin = ""
#         self.color = "White"

#     def drive(self):
#         print("driving....")

#     def brake(self):
#         print('brake...')

#     def putFuel(self):
#         print('Put gasoline in car...')

#     def changeGear(self, gearNo):
#         print(f'changing gear to {gearNo}')

# # def updateColor


# car = Car('Honda', 'Accord')
# print(car.color)


# car.drive()



# Creating a Class 

class Car: 
    def __init__(self, make, model): # initializer/constructor 
        # define properties of the car 
        self.make = make 
        self.model = model 
        self.color = "White" 
        self.vin = ""

    def putFuel(self): 
        print("Put gasoline in car...")

    def updateColor(self, color): 
        # check if the color is available 

        # then apply the color 
        self.color = color

    def drive(self): 
        print("driving....")

    def changeGear(self, gearNo): 
        print(f"changing gear to {gearNo}")


    def brake(self): 
        print("brake..")


car = Car("Honda", "Accord")
print(car.color)
#car.color = "Dark Gray"
car.updateColor("Dark Gray")
print(car.color)

car2 = Car("Honda", "Accord")
car2.color = "Black"



print(car.drive()) 
car.brake() 
car.putFuel()
car.changeGear(2) 


class ElectricCar(Car): #inheritance ElectricCar is inheriting from Car class/can inherit from multiple classes(will become more confusing)
    
    def __init__(self, make, model):
        super().__init__(make, model) # call initializer of the super/parent (Car) class
        self.battery = 100
        self.range = 300

    # override putFuel function
    def putFuel(self):
        print('Charge car....')

tesla = ElectricCar("Tesla", "Model 3")

tesla.putFuel()
print(tesla.make)
print(tesla.brake)
print(tesla.model)

print(tesla.range)

print('Array...')
cars = []
car10 = Car('Honda', 'Accord')
cars.append(car10) 
print(cars[0].make)
cars[0].make = "Tesla"
print(car10.make)

car20 = car10
car20.make = 'Truck'

print(car10.make)