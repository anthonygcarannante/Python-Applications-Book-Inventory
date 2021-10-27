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

    def __init__(self,filepath):
        # Call instance of Account class, so sub-class is created from Account class, passing the same parameters needed for the Account class
        Account.__init__(self, filepath)

    def transfer(self,amount):
        self.balance=self.balance - amount

checking=Checking("account/balance.txt")
print(checking.balance)
checking.transfer(150)
checking.commit()
print(checking.balance)