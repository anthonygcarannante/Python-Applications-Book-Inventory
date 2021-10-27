class Account:

    def __init__(self,filepath):
        with open(filepath, 'r') as file:
            self.filepath=filepath
            # Save value from text file in instance variable (self is object, balance is instance variable stored in object)
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# Create inheritance classes Checking and Savings. Pass Base Class as variable into inherited class
class Checking(Account):
    # Doc string - text explaining function of the class
    """This class generates checking account objects"""

    type="checking"
    def __init__(self,filepath,fee):
        # Call instance of Account class, so sub-class is created from Account class, passing the same parameters needed for the Account class
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee

jacks_checking=Checking("account/jack.txt",1)
jacks_checking.transfer(100)
jacks_checking.commit()
print(jacks_checking.balance)
print(jacks_checking.type)

johns_checking=Checking("account/john.txt",1)
johns_checking.transfer(100)
johns_checking.commit()
print(johns_checking.balance)
# class variable - shared by all instances of the class
print(johns_checking.type)

# Prints doc string for explanation of classes
print(johns_checking.__doc__)

