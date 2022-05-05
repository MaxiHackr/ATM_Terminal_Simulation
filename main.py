import random
import time

print("Welcome to Maxi Bank ATM")

n = 1000
restart = 'Y'
chances = 3
balance = n * random.random() + 1

while chances >= 0:
    pin = int(input("Please Enter your 4 Digit Pin Code: "))
    if pin in [1234, 4356, 1245, 5678, 9812, 1516, 9240, 2016, 2022]:
        print("\nYou have entered your PIN correctly.\n")
        while restart not in ("n", "NO", "No", "no", "N"):
            print("Please press option 1 to view your balance.\n")
            print("Please press option 2 to make a withdrawal.\n")
            print("Please press option 3 to make a deposit.\n")
            print("Please press option 4 to return your card.\n")
            option = int(input("What would you like to choose?: "))
            if option == 1:
                print(f"Your balance is £{round(balance)}\n")
                restart = input("Would you like to go back? (Y/N): ")
                if restart in ("n", "NO", "No", "no", "N"):
                    print("Thank you for using Maxi Bank ATM's")
                    break
            elif option == 2:
                option2 = ('y')
                print(f"Current balance: £{round(balance)}\n")
                withdrawal = int(input("How much would you like to withdraw?\n £10|£20|£30|£40|£50|£60|£70|£80|100\n"))
                if withdrawal in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300]:
                    balance = balance - withdrawal
                    print(f"Your balance is now: £{round(balance)}\n")
                    restart = input("Would you like to go back? (Y/N): ")
                    if restart in ("n", "NO", "No", "no", "N"):
                        print("Thank you for using Maxi Bank ATM's")
                        break
                    elif withdrawal != [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300]:
                        print("Invalid amount, Please try again.")
                        restart = ('y')
                    elif withdrawal == 1:
                        withdrawal = int(input("Please enter desired amount: "))
                    elif withdrawal > balance:
                        print("You do not have sufficient funds for that transaction, please try again")
                        restart = ('y')
            elif option == 3:
                deposit = int(input("Please input the amount in multiples of 10, that you would like to deposit"))
                if deposit in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300]:
                    print(f"You have deposited £{deposit}\n")
                    balance = balance + deposit
                    print(f"Your new balance is {balance}\n")
                    restart = input("Would you like to go back? (Y/N): ")
                    if restart in ("n", "NO", "No", "no", "N"):
                        print("Thank you for using Maxi Bank ATM's\n")
                        break
                elif deposit not in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300]:
                    print("Please enter a valid amount, try again.")
                    restart = ('y')
            elif option == 4:
                print("Dispensing card, please wait")
                time.sleep(5)
                print("Thanks for using Maxi Bank ATM's.\nGood Bye")
                break
            else:
                print("Please enter a correct PIN")
    elif pin != [1234, 4356, 1245, 5678, 9812, 1516, 9240, 2016, 2022]:
        print("Incorrect PIN")
        chances = chances - 1
        if chances == 0:
            print("No more chances, your card is now locked.")
            break



