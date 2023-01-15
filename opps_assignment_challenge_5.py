class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance-=amount
        pass

    def deposit(self, amount):
        self.balance+=amount
        pass
    def getBalance(self):
        return self.balance
        pass

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        return self.balance*(self.interestRate/100)
        pass



demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print(demo1.getBalance())
demo1.withdrawal(500)
print(demo1.getBalance())
print(demo1.interestAmount())