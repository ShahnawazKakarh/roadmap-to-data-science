class Account:

    # Constructor method: Called when creating a new instance of the class
    # Initialize the account with account number, holder's name, and initial balance
    def __init__(self, account_number, account_holder, balance=0):

        # self refers to the current instance of the class
        # Refers to the current instance: When a method is called on an object,
        # self provides access to that specific object's attributes and methods.
        # This allows methods to manipulate the state of the particular instance they are called upon.

        # Initialize instance variables
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

# Add methods to deposit, withdraw, and check balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            # print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
            # .2f is used to format the float to 2 decimal places
            print("Deposited: ${:.2f}. New balance: ${:.2f}".format(amount, self.balance))

        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew: ${:.2f}. New balance: ${:.2f}".format(amount, self.balance))
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Display the account details
    def display_account(self):
        print("Account Number: ${:.2f}, Balance: ${:.2f}".format(self.account_number, self.balance))
        
# # Inheriting from Account class to create a SavingsAccount class
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        # super() is used to call the constructor of the parent class (Account) goes in Account init,
        # as we have defined the parameters to define it as it
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print("Applied interest:: ${:.2f}. New balance: ${:.2f}".format(interest, self.balance))

    # Polymorphism: Overriding the display_account method
    # Display the account details
    def display_account(self):
        print("Savings Account Number: ${:.2f}, Balance: ${:.2f} Interest Rate: ".format(self.account_number, self.balance, self.interest_rate))

    # New method specific to SavingsAccount for adding interest
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print("Interest added: ${:.2f}. New balance: ${:.2f}".format(interest, self.balance))

## Inheritance: Current Account Inheriting from Account class
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Overriding the withdraw method to include overdraft functionality
    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrew: ${:.2f}. New balance: ${:.2f}".format(amount, self.balance))
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Polymorphism: Overriding the display_account method
    def display_account(self):
        print("Current Account Number: ${:.2f}, Balance: ${:.2f}, Overdraft Limit: ${:.2f}".format(self.account_number, self.balance, self.overdraft_limit))
        
        



    

