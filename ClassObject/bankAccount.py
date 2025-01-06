
class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to Simple Deposite and Withdraw Machine")

    def deposite(self):
        amount = float(input("Enter amount to be Deposited:"))
        self.balance += amount
        print("\n Deposited amount:",amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdraw:"))

        if self.balance>=amount:
            self.balance -= amount
            print("\n Withdraw amount:", amount)
        else:
            print("\n Insufficient balance")

    def check_balance(self):
        print("\n Net Available Balance:",self.balance)

bankaccount = BankAccount()
bankaccount.deposite()
bankaccount.withdraw()
bankaccount.check_balance()