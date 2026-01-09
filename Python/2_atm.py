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
            print("Create pin")
        elif user_input == "2":
            print("Deposit")
        elif user_input == "3":
            print("Withdraw")
        elif user_input == "4":
            print("Check Balance")
        else:
            print("Bye Bye !!! Exited")


sbi = Atm()
print(sbi)

