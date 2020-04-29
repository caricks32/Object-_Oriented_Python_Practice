
class Account():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self):
        cash = 0

        cash = int(input("Insert amount to withdraw $: "))
        if self.balance - cash < 0:
            print("Oops! Your account cannot be overdrawn")
            print("This transaction would make your balance: ${}\n\n\n\n\n\n".format(self.balance - cash))
        else:
            self.balance -= cash
            print("Your balance is now ${}\n\n\n\n\n\n".format(self.balance))

    def deposit(self):
        cash = 0

        cash = int(input("Insert amount to deposit $: "))

        self.balance += cash
        print("Your balance is now ${}\n\n\n\n\n\n".format(self.balance))

    def check_balance(self):
        print("-------------------------")
        print("Your balance is: ${}\n\n\n\n\n\n".format(self.balance))
        print("-------------------------\n\n")


    def printHeading(self):
        print("----------------------")
        print("Welcome to Ricks Bank")
        print("----------------------\n\n\n\n\n\n")

    def printMenu(self):
        choice = 0

        print("1.) Deposit")
        print("2.) Withdraw")
        print("3.) Check Balance")
        print("4.) Exit")
        print("---------------------")



choice = 0
my_account = Account('Emily', 1000)
my_account.printHeading()

while True:
    my_account.printMenu()
    while True: # Verify the user entered an integer. Also verify their input is a menu option
        try:
            choice = int(input("Please select an option [1-4]: "))
            if choice == 1:
                my_account.deposit()
                break
            elif choice == 2:
                my_account.withdraw()
                break
            elif choice == 3:
                my_account.check_balance()
                break
            elif choice == 4:
                print("Thank you for choosing Ricks Bank! Goodbye!\n\n\n\n\n\n")
                exit()
            else:
                print("Oops! That option does not exist!\n\n")
        except ValueError: # The user entered a value that is not an integer
            print("Oops! That option does not exist!\n\n")






