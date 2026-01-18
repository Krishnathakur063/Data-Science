class demo:
    
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

        print("This is the ID of self: ",id(self))

    def menu(self):
        user_input = input("""
                        Hello, how would you like to proceed ?
                        1. Enter 1 to create pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit
                    """)



sbi = demo()

print("Id of SBI: ", id(sbi))

hdfc = demo()

print("Id of hdfc: ", id(hdfc))

# It means self is an object, we are currently working with.
