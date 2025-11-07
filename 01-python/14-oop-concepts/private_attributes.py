## Encapsulation is a fundamental concept in object-oriented programming (OOP) that involves bundling data (attributes)
# and methods (functions) that operate on that data into a single unit, known as a class.
class Account:
    ## Constructor to initialize account details
    ## 
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number ## Private attribute
        self.account_holder = account_holder
        self.__balance = balance ## Private attribute

    ## Add the money to the account
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    ## Withdraw the money from the account
    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print(f"{amount} withdrawn")
        else:
            print("Insufficient Funds")
    
    ## Display the account details
    def display(self):
        print(f"Account Number: {self.__account_number}, Balance: {self.__balance}")

if __name__=='__main__':
    acc1 = Account("27834877776502", "Junaid Younas", 10000)
    ## print(acc1.__balance)
    print(acc1.__account_number)  ## This will raise an AttributeError: 'Account' object has no attribute '__account_number'
    acc1.deposit(20000)
    acc1.withdraw(2000)
    acc1.display()
