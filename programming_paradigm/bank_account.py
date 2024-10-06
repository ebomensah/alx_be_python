class BankAccount: #Create account
    def __init__ (self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited {$amount: .2f}") 
        
    def withdraw(self, amount):        
        self.account_balance -= amount
        print(f"Withdrew {$amount: .2f}")
        return True
        if self.account_balance < amount:
            print ("Insufficient funds for this withdrawal.")
            return False
            
    def display_balance(self):
        print(f"Current Balance:{$self.account_balance: .2f}")
