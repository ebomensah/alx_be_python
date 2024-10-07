class BankAccount: #Create account
    def __init__ (self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited ${amount:,.2f}") 
        
    def withdraw(self, amount):        
        if amount <= self.account_balance and amount > 0:
            self.account_balance -= amount
            return True
        elif amount > self.account_balance:
            print("Insufficient funds.")
            return False
                        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:,.2f}")


if __name__ == "__main__":
    account = BankAccount(100)
account.withdraw(1000)
account.display_balance()