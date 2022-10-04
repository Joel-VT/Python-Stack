class BankAccount:
    all_accounts = []
    def __init__(self, type, interest_rate, balance=0):
        self.type = type
        self.balance = balance
        self.interest_rate = interest_rate/100
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"{self.type} Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

    def return_balance(self):
        return self.balance
    

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print("=======================")
            print(f"Type: {account.type}")
            print(f"Balance: ${account.balance}")
            print(f"Interest Rate: {int(account.interest_rate*100)}%")
            print("=======================")


class User:
    all_users = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings_account = BankAccount("Savings", 2)
        self.checking_account = BankAccount("Checking", 2)
    
    def make_deposit(self, type, amount):
        if type.lower() == "savings":
            self.savings_account.deposit(amount)
        elif type.lower() == "checking":
            self.checking_account.deposit(amount)
        else:
            print("Invalid Account Type: Choose either Checking or Savings")
        return self
    
    def make_withdrawal(self, type, amount):
        if type.lower() == "savings":
            self.savings_account.withdraw(amount)
        elif type.lower() == "checking":
            self.checking_account.withdraw(amount)
        else:
            print("Invalid Account Type: Choose either Checking or Savings")
        return self
    
    def display_user_balance(self):
        print("=======================")
        print(f"User: {self.name}", end = "\t")
        self.savings_account.display_account_info()
        print(f"User: {self.name}", end = "\t")
        self.checking_account.display_account_info()
        print("=======================")
        return self

    def transfer_money(self, type, amount, other_user):
        if type.lower() == "savings":
            if self.savings_account.return_balance() - amount >= 0:
                self.savings_account.withdraw(amount)
                other_user.checking_account.deposit(amount)
                print(f"Successfully transfered {amount} to {other_user.name}")
            else:
                print(f"Transfer Unsuccessful. Insufficient Balance in {type} account")
        elif type.lower() == "checking":
            if self.checking_account.return_balance() - amount >= 0:
                self.checking_account.withdraw(amount)
                other_user.checking_account.deposit(amount)
                print(f"Successfully transfered ${amount} to {other_user.name}")
            else:
                print(f"Transfer Unsuccessful. Insufficient Balance in {type} account")
        else:
            print("Invalid Account Type: Choose either Checking or Savings")


new_user = User("Joel","joelvarghese90@gmail.com")
new_user.make_deposit("Savings",100).make_deposit("Checking",300).make_withdrawal("Checking",1000).display_user_balance()

new_user2 = User("Thomas","thomasv01@gmail.com")
new_user2.make_deposit("Savings",1000).make_deposit("Checking",3000).make_withdrawal("Checking",1000).display_user_balance()

new_user2.transfer_money("Checking",1000,new_user)
new_user2.display_user_balance()

new_user.display_user_balance()

# new_account = BankAccount(2)

# new_account2 = BankAccount(5,100)

# new_account.deposit(300).deposit(50).deposit(100).withdraw(400).yield_interest().display_account_info()

# new_account2.deposit(300).deposit(50).withdraw(50).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

# BankAccount.display_all_accounts()