class Account:
    def __init__(self,bal,account):
        self.Balance=bal
        self.account_no=account
    
    def credit(self,amount):
        self.Balance+=amount
        print("The amount ",amount," is Credited in your Account ",self.Show_amount())

    def debit(self,amount):
        self.Balance-=amount
        print("The amount ",amount," is Debited from your account ",self.Show_amount())

    def Show_amount(self):
       return self.Balance

a1=Account(10000,1234567)
a1.credit(40000)
a1.debit(30000)