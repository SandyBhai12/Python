class Account:

    def __init__(self,balance,accountNum):
        self.balance=balance
        self.accountNum=accountNum

    def debit(self,amount):
        self.balance -=amount
        print("After debiting the amount your balance is = ",self.balance)
    def credit(self,amount):
        self.balance +=amount
        print("After crediting the amount your balance is = ",self.balance)

    def showBalance(self):
        print(" your balance is = ",self.balance)

a1=Account(10000,56252)

a1.debit(500)
a1.credit(5000)
a1.showBalance()
