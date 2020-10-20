 #banking system with options like Name, acc. no, Initial amount, withdrawal, deposit, check balance, exit.
upi=4554
#welcome
class bank:
    def __init__(self, InA):
        self.InA= InA

    def index(self):
        x=eval(input("Press 1 to withdraw\nPress 2 to deposit\nPress 3 to Know balance\nPress 4 to Exit \n"))
        if(x==1):
            self.withdraw()
        elif(x==2):
            self.deposit()
        elif(x==3):
            self.bal()
        elif(x==4):
            print("Bye bye!")
        else:
            print("Invalid Input")
            self.index()

    def withdraw(self):
        withdraw=eval(input("Enter the amount to withdraw\n"))
        temp1=eval(input("Enter your upi pin:\n"))
        if(temp1==upi):
            self.InA=self.InA-withdraw
            print("Transaction Successful :) \n")
            print("You have:",self.InA,"\n")
            self.index()
        else:
            print("Are you the real one? >:(>:(")
            
    def deposit(self):
        deposit=eval(input("Enter the amount to deposit\n"))
        temp2=eval(input("Enter UPI pin\n"))
        if(temp2==upi):
            self.InA=self.InA+deposit
            print("Transaction Successful :) \n")
            print("Amount left: ",self.InA,"\n")
            self.index()
        else:
            print("Are you the real one? >:(>:(")
            self.index()
            
    def bal(self):
        temp3=eval(input("Enter the UPI pin\n"))
        if(temp3==upi):
            print("Balance is:\n",self.InA)
            self.index()
        else:
            print("Are you the real one? >:(")
            self.index()

p1=bank(10000)
p1.index()
