#Mason Chandler
#Level 08 Assignment

import random
#A template to what something is
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(1000, 2000)
        self.balance = 0.0
    def __str__(self):
        return f"Account owner: {self.name}, Balance: ${self.balance:.2f}"




# Make a deposit
def deposit(account):
    while True:
        try:
            amount = float(input("Enter deposit amount: "))
            if amount >= 0:
                account.balance += amount
                print (f'New Balance: ${account.balance:.2f}')
                return
            print("Input must be a number and greater than 0")
        except ValueError:
            print("Input must be a number and greater than 0")

# Make a withdrawal
def withdraw(account): 
    while True: 
        try:
            amount = float(input("How much to withdraw: "))
            if amount < 0:
                print("Input must be a number and greater than 0")
            elif amount > account.balance:
                print ("Insufficient Funds")
            else:
                account.balance -= amount
                print(f'Remaining Balance: ${account.balance:.2f}')
                return
        except ValueError:
            print("Input must be a number and greater than 0")


# View account information
def view_account(account):
    print(f"Name: {account.name}")
    print(f"Account Number: {account.account_number}")
    print(f"Account Balance: ${account.balance:.2f}")