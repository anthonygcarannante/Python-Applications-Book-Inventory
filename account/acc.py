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


# Run class, passing the path of the text file
account=Account("account/balance.txt")

# Print instance of balance variable
print(account.balance) 
account.withdraw(100)
print(account.balance)
account.commit()