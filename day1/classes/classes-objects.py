
class Restuarant:

    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.itemsOrdered = 0

    def orderItem(self):
        self.itemsOrdered += 1

    def displayOrderStatus(self):
        print('We ordered ' + str(self.itemsOrdered) + "And item was " + self.title)

    def print_description(self):
        print(self.title + self.description)

res = Restuarant('Burger King','Burgers')
res.orderItem()
res.orderItem()

print(res.displayOrderStatus())



class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = ""
        self.age = -1
        self.height = 0
        self.weight = 0

    def walk(self):
        print("person is walking")

    def talk(self):
        print("person is talking")

    def sing(self,songName):
        print("Person is singing " + songName)


person1 = Person('John','Doe')
person1.age = 23
person1.weight = 190

person1.walk()
person1.talk()
person1.sing("Song Name")






class Car:

    def __init__(self,make,model):
        self.make = make
        self.model = model
        self.noOfCylinders = 4

    def start(self):
        print("Starting Car")


audi = Car('Audi','Series 4')
audi.model = 'Series 5'


bmw = Car('BMW','Series 3')
#print(bmw.make)
#print(bmw.model)
bmw.make = "Audi"
bmw.model = "Series 4"

#print(bmw.noOfCylinders)
bmw.start()

toyota = Car('Toyota','Camry')
#print(toyota.make)
#print(toyota.model)
