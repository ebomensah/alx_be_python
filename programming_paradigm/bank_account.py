class BankAccount: #Create account
    def __init__ (self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return(f"Deposited ${amount:,.2f}") 
        
    def withdraw(self, amount):        
        if amount <= self.account_balance:
            self.account_balance -= amount
            return(f"Withdrew ${amount:,.2f}")
        else:
            return ("Insufficient funds.")
            
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:,.2f}")
