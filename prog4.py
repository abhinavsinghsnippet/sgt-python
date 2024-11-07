'''4. Bank Account
•	Create a class called BankAccount with the following attributes:
o	account_holder: Name of the account holder.
o	balance: Account balance (default is 0).
•	Write methods for:
o	deposit(amount): Adds money to the balance.
o	withdraw(amount): Deducts money from the balance, ensuring the balance doesn’t go negative.
o	display_balance(): Shows the current balance.
•	Create an instance of BankAccount, deposit some money, withdraw an amount, and check the balance.'''
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def display_balance(self):
        print(f"Current balance: {self.balance}")


account = BankAccount("Abhinav singh", 1000)
account.deposit(500)
account.withdraw(200)
account.display_balance()
