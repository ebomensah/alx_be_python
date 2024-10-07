class BankAccount: #Create account
    def __init__ (self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return(f"Deposited ${amount:,.2f}") 
        
    def withdraw(self, amount):        
        if self.account_balance > amount:
            self.account_balance -= amount
            return(f"Withdrew ${amount:,.2f}")
        elif amount > initial_balance:
            return ("Insufficient funds.")
            return False
            
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:,.2f}")
