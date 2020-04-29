



class Address: 
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class User:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.address = []


user = User()
user.firstName = "Ricky"
user.lastName = "Paige"

address1 = Address("10326 Lighthouse Ln", "Missouri City", "Texas", "77459")
address2 = Address("4325 W. Rome Blvd", "North Las Vegas", "Nevada", "89084")

user.address.append(address1)

print(user.firstName + " " + user.lastName)
for address in user.address: 
    print(address.street + " " + address.state)
    print("\n")

user.address.append(address2)

print(user.address)




class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person('John', 'Doe')

x.printname()


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = 2015
    
    def printPerson(self):
        print(self.firstname, self.lastname, self.graduationyear)




x = Student('Ricky', 'Paige', 2015)
x.printPerson()