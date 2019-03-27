class Accounts(object):
    types = ('ASSET','LIABILITY','INCOME','EXPENSE','OE')
    accounts = 0

    def __init__(self,balance=0,atype=0):
        self.balance = balance
        self.type = atype
        Accounts.accounts +=1
        self.accno = Accounts.accounts

    def debit(self,amount):
        if self.type in [0,3]:
            self.balance += amount
        else:
            self.balance -= amount

    def credit(self,amount):
        self.debit(-amount)

    def __str__(self):
        return "Account no %d" % self.accno

class CreditAccounts(Accounts):
    def __init__(self,**kwargs):
        Accounts.__init__(self,**kwargs)
        self.creditLimit = 0

    def debit(self,amount):
        assert self.type in [0,3] and amount >0 \
            and self.balance + amount < self.creditLimit, \
            "credit limmit exceeded"
            
        assert self.type in [1,2,4] and amount <0 \
            and self.balance - amount < self.creditLimit, \
            "credit limmit exceeded"
        Accounts.debit(self, amount)

if __name__ == "__main__":
    current = Accounts()
    credit = CreditAccounts(balance=1000,atype=1)
    print(isinstance(credit,CreditAccounts))
    print(credit.creditLimit)
    print(current.__dict__)
    print(current.__class__)
    current.debit(10)  #Accounts.debit(current,10)
    credit.debit(100)  #Accounts.debit(credit,100)
    print(current.balance)
    print(credit.balance)
