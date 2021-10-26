class Account:

    def __init__(self,filepath):
        with open(filepath, 'r') as file:
            # Save value from text file in instance variable (self is object, balance is instance variable stored in object)
            self.balance=int(file.read())

# Run class, passing the path of the text file
account=Account("account/balance.txt")

# Print object
print(account)

# Print instance of balance variable
print(account.balance)