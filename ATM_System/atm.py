#Check balance
#Deposit money
#Withdraw money
#Transaction history
#Logout securely

class Bank:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
        self.transactions=[]
    def view(self):
        print(f"Account Holder: {self.name}")
        print(f"Amount: {self.balance}")
    def deposit(self,amt):
        self.balance+=amt
        self.transactions.append(f"Deposited: {amt}")
        print(f"Your amount {amt} has been successfully deposited.")
        print(f"Total amount: {self.balance}")
    def withdraw(self,amt):
        if amt>self.balance:
            print("Invalid amount")
        else:
            self.balance-=amt 
            self.transactions.append(f"Withdrawn: {amt}")
            print(f"Your amount {amt} has been successfully withdrawn")
            print(f"Remaining Amount: {self.balance}")
    def history(self):
        print("Transaction History")
        for t in self.transactions:
            print("-",t)
    def logout(self):
        print("Logged Out successfully")
bank=Bank(1234567,'Harshi',10000)
while True:
    print("Operations: 1.View Account 2.Deposit 3.Withdraw 4.Transaction History 5.Logout")
    choice=int(input("Enter the operation to perform: "))
    if choice==1:
        bank.view()
    elif choice==2:
        d=int(input("Enter amount to be deposited: "))
        bank.deposit(d)
    elif choice==3:
        w=int(input("Enter the amount to be withdrawn: "))
        bank.withdraw(w)
    elif choice==4:
        bank.history()
    elif choice==5:
        bank.logout()

        break
