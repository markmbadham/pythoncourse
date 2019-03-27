class Accounts(object):
    types = ('ASSET','LIABILITY','INCOME','EXPENSE','OE')
    accounts = 0

    def __init__(self,balance=0,atype=0):
        self.balance = balance
        self.type = atype

    def debit(self,amount):
        if self.type in [0,3]:
            self.balance += amount
        else:
            self.balance -= amount

    def credit(self,amount):
        self.debit(-amount)

if __name__ == "__main__":
    current = Accounts()
    credit = Accounts(1000,atype=1)
    print(current.__dict__)
    print(current.__class__)
    current.debit(10)  #Accounts.debit(current,10)
    credit.debit(100)  #Accounts.debit(credit,100)
    print(current.balance)
    print(credit.balance)
