#Mason Chandler
#Level 08 Assignment

from Level8functions import *

print ("Welcome to the PBR Bank")

name = input("Please enter your name: ")
account = BankAccount(name)

while True:
    print("\n Please choose an option: ")
    print("1. Make a Deposit")
    print("2. Make a Withdrawal")
    print("3. View your information")
    print("4. Quit")

    choice = input("Enter number here: ")

    if choice == "1":
        deposit(account)
    elif choice == "2":
        withdraw(account)
    elif choice == "3":
        view_account(account)
    elif choice == "4":
        print("Have a good day, goodbye!")
        break
    else:
        print("Invalid choice, enter 1, 2, 3, or 4")