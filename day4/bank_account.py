class BankAccount:
    def __init__(self):
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, destination, amount):
        destination.deposit(amount) # deposit money into destination account  
        self.withdraw(amount) # subtract $ from the source amount