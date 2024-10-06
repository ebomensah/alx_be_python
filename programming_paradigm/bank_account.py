class BankAccount: #Create account
    def __init__ (self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount}") 
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if self.account_balance < amount:
            print("Insufficient funds")
        else:
             self.account_balance -= amount
             print(f"Withdraw: ${amount}")
    def display_balance(self):
        print(f"Current Balance : ${self.account_balance}")
