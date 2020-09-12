Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

class bank():
    ownername = "Jay Shukla "
    balance = 2332

    def updatebalance(self,updatebalance):
        self.updatebalance = updatebalance
    def __init__(self,ownername,balance):
        self.ownername = ownername
        self.balance = balance
    def deposite(self):
        print("amount deposite- ", self.deposite)
    def withdraw(self):
        self.withdraw = withdraw
        if balance <= 2000:
            print("balance is low, kindly maintane you account")
        else:
            print("your balance is", balance)
            class Rahul(bank):
                def __init__(self, ownername, balance):
                    print("Rahul created a account")
                class Bank_Account:
                    def __init__(self):
                        self.balance = 0
                        print("Welcome to Mani Bank")

                    def ownername(self):
                        ownername = str(input("Enter you name: "))
                        self.ownername = ownername
                        print("\n Wlecome mr./miss", ownername)

                    def deposit(self):
                        amount = float(input("Enter amount to be Deposited: "))
                        self.balance += amount
                        print("\n Amount Deposited:", amount)

                    def withdraw(self):
                        amount = float(input("Enter amount to be Withdrawn: "))
                        if self.balance >= amount:
                            self.balance -= amount
                            print("\n You Withdrew:", amount)
                        else:
                            print("\n Insufficient balance  ")

                    def display(self):
                        print("\n Net Available Balance=", self.balance)