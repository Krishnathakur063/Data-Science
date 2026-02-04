
class Atm:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.__menu()
    
    def __menu(self):
        user_input = input("""
                        Hello, how would you like to proceed ?
                        1. Enter 1 to create pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit
""")
        if user_input == "1":
            self.create_pin()
            # print("Create pin")

            self.menu()

        elif user_input == "2":
            self.deposit()
            # print("Deposit")

            self.menu()

        elif user_input == "3":
            self.withdraw()
            # print("Withdraw")

            self.menu()


        elif user_input == "4":
            self.check_balance()
            # print("Check Balance")

            self.menu()

        else:
            print("Bye Bye !!! Exited")

    def create_pin(self):
        self.__pin = input("Enter your pin ")
        print("Pin set successfully !!!")

    def deposit(self):
        temp = input("Enter you pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount "))
            self.__balance = self.__balance + amount
            print("Deposit sucessfull !!!")
        
        else:
            print("Invalid PIN")

    def withdraw(self):
        temp = input("Enter you pin ")
        if temp == self.__pin:
            amount = int(input("Enter the amount "))

            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw sucessfull !!!")

            else:
                print("Insufficient Funds !!!")

        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter you pin ")

        if temp == self.__pin:
            print(self.__balance)
        
        else:
            print("Invalid PIN")





sbi = Atm()
print(sbi)

# Nothing in python is truly private.

# sbi.balance ="dfasdsfsd"
# sbi.deposit()

# This code wil run.

# sbi.__balance = 'dsjfasnsd'
# sbi.deposit()
# sbi.check_balance()


# Note:- Python is looking this code as "_Atm__pin" and "_Atm__balance"

# sbi._Atm__balance = "wgwh"
# sbi.deposit()

# Now code will crash.

# Need of Encapsulation:- We can not leave data openly so anyone can do changes 
# in data. So first we have make variable private by adding double underscore.
# For e.g:- __pin, __balance.
# And we also create getter and setter method to access the private data if it
# is necessary to access them.



