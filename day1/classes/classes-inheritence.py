
class Animal(object):

    def __init__(self,name,species):
        self.name = name
        self.species = species

    def run(self):
        print("running like a normal animal")

    def walk(self):
        print("I am walking")

    def eat(self):
        print("I am eating")


class Cheetah(Animal):

    def __init__(self):
        # calling the Animal class initializer/constructor
        super(Cheetah,self).__init__('Cheetah','Cats')
        self.name = ""
        
    def run(self):
        print("Cheetah is running super fast")


# creating an object of Animal class
cat = Animal('Lync','Cat Species')
cat.walk()
cat.eat()

ch = Cheetah()
ch.run()
ch.walk()
ch.eat()
