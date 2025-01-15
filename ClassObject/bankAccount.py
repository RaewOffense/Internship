from context_manager import ContextManager
import csv
class BankAccount:
    def __init__(self):
        self.balance = 0
        

    def deposit(self):
        try:
            #Read current balance
            with ContextManager("deposit.csv", "r") as deposit:
                reader = csv.reader(deposit)
                next(reader) 
                for row in reader:
                    self.balance = float(row[0])  
        except FileNotFoundError:
            print("No existing balance file found. Starting fresh.")
            self.balance = 0
        except Exception as e:
            print(f"Error reading the file: {e}")
    
        try:
            amount = float(input("Enter amount to be Deposited: "))
            self.balance += amount
            print("\nDeposited amount:", amount)
    
            #update the balance
            with ContextManager("deposit.csv", "w") as deposit:
                writer = csv.writer(deposit)
                writer.writerow(["Balance"])
                writer.writerow([self.balance])
            print(f"Updated Balance: {self.balance}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"Error updating the file: {e}")
    
    
    def withdraw(self):
        amount = float(input("Enter amount to be Withdraw:"))

        try:
            with ContextManager("deposit.csv","r") as deposit:
                reader = csv.reader(deposit)
                next(reader) 
                for row in reader:
                    self.balance = float(row[0])  
        except FileNotFoundError:
            print("No existing balance file found. Starting fresh.")        

        if self.balance>=amount:
            self.balance -= amount
            print("\n Withdraw amount:", amount)
            print(f"\n Remaining Balance is {self.balance}")
        else:
            print("\n Insufficient balance")
        try:
            with ContextManager("deposit.csv", "w") as deposit:
                writer = csv.writer(deposit)
                writer.writerow(["Balance"])
                writer.writerow([self.balance])
                print(f"Updated Balance: {self.balance}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"Error updating the file: {e}")

    def check_balance(self):
        try:
            with ContextManager("deposit.csv","r") as deposit:
                reader = csv.reader(deposit)
                next(reader) 
                for row in reader:
                    self.balance = float(row[0])  
                print("\n Net Available Balance:",self.balance)
        except FileNotFoundError:
            print("No existing balance file found. Starting fresh.")
        

class Main(BankAccount):
    def display(self):
        while True:
            print("Welcome to Simple Deposit and Withdraw Machine")
            print("""
            1. Deposit Money
            2. Withdraw Money
            3. Check Money
            4. Exit
            """)

            try:
                choice = int(input("What Do You Want To Do?:"))
                if choice == 1:
                    self.deposit()
                
                elif choice == 2:
                    self.withdraw()
                elif choice == 3:
                    self.check_balance()
                elif choice == 4:
                    print("Good Bye!!!")
                    break
                else:
                    print("Invalid Choice,Please Enter a valid Choice(1-4).")
            except ValueError:
                print("Invalid Choice, Please choose only numeric value")

mainObject =Main() 
mainObject.display()
