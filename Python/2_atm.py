# Functions Vs Methods => Methods is a special function which are inside the class.
# Functions are not inside the class.

# print(len(L)) # => This is a Function.
# print(L.append(1)) => This is a method.

class Atm:
#  when we have to declare some variable in the class then we have to declare
#  inside the __init__(self) constructor.

# Constructor:- Constructor is a special method inside the class which will automatically
#  execute when the object of class is created.

    # def __init__(self):
    #     print("Hello")

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    
    def menu(self):
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

        elif user_input == "2":
            self.deposit()
            # print("Deposit")

        elif user_input == "3":
            self.withdraw()
            # print("Withdraw")

        elif user_input == "4":
            self.check_balance()
            # print("Check Balance")

        else:
            print("Bye Bye !!! Exited")

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter you pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit sucessfull")
        
        else:
            print("Invalid PIN")

    def withdraw(self):
        temp = input("Enter you pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))

            if amount < self.balance:
                self.balance = self.balance - amount
                print("Withdraw sucessfull")

            else:
                print("Insufficient Funds")

        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter you pin")

        if temp == self.pin:
            print(self.balance)
        
        else:
            print("Invalid PIN")





sbi = Atm()
print(sbi)

