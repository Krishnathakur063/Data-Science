
class Atm:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.__menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("PIN Changed")
        else:
            print("Not allowed")

    
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


# Atm()

# when we are creating object by calling simply 'Atm()' class. Buy we can not use it.
# Because at the time of object creation we did not store it into any variable.
# Because of that not this object is lost in memory.

# So that's why we write below code for object creation.

# sbi = Atm()
# print(sbi)

# Now in above code 'sbi' is holding the reference (address) of 'Atm()' class object. 
# Technically 'sbi' is not an object. It's a variable which point out the
# reference (address) of 'Atm()' class object. So that's why we called it
# reference variable. So here 'sbi' is a reference variable.


# 
#  Pass by reference 
# 

class Customer:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name, "Sir")
    else:
        print("Hello", customer.name, "ma'am")
    
    cust2 = Customer("Krishna", "Male")
    return cust2


cust = Customer('Ankita', 'Female')
# print(cust.name)
# greet(cust)

# new_cust = greet(cust)
# print(new_cust.name)

# So by seeing this now we can conclude that our own class object we can pass as an arguement in funcation.
# And function can also return the object.


# --------------------- Pass By Reference -----------------------------------

class Customer1:

    def __init__(self, name):
        self.name = name
    


def greeting(customer):
    print(id(customer))

cust1 = Customer1("Krisna")
# print(id(cust1))
# greeting(cust1)

# ----------------------------

class Customer2:

    def __init__(self, name):
        self.name = name
    


def greeting(customer):
    print(id(customer))
    customer.name = "Jadaun"
    print(customer.name)
    print(id(customer))

cust2 = Customer2("Krisna")
print(id(cust2))
greeting(cust2)

# In python class objects are also mutable like lists, dict, and sets.
