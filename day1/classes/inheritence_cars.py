

class Car(object):
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def start(self):
        print("Starting the gas car")

class ElectricCar(Car):
    def __init__(self):
        super(ElectricCar,self).__init__('Tesla','X')

    # overriding the start method from the super/parent/base class
    def start(self):
        print("starting the electric car")

electric_car = ElectricCar()
print(electric_car.make)
print(electric_car.model)
electric_car.start()
