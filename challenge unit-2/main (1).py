class Bank_Account:
    def name(self):
        
        print("Account holder name: A.L. Subalakshmi")
        print("Account no: 218164818184894")
    def __init__(self): #initialize the const
        self.balance=0
        print("Welcome to Bank")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrow:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        print("\n Net Available Balance=",self.balance)
r=Bank_Account()
r.name()
r.deposit()
r.withdraw()
r.display()