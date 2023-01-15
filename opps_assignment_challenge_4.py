class Account:
    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance
class SavingsAccount(Account):
    def __init__(self,title=None,Balance=0,interestRate=0):
        super().__init__(title,Balance)
        self.interestRate=interestRate
a=Account('Ashish',5000)
s=SavingsAccount('Ashish',5000,5)

