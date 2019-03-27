class Account(object):
    accounts = 0
    def __init__(self,balance=0):
        self.balance = balance
        Account.accounts +=  1
        self.accno = Account.accounts

    def debit(self,amount):
        self.balance -= amount

    def credit(self,amount):
        self.balance += amount

class CreditAccount(Account): 
    def __init__(self,balance=0, credit_limit=0): 
        Account.__init__(self,balance)
        self.credit_limit=credit_limit

    def debit(self,amount):
        assert amount < self.balance + self.credit_limit, 'account overdrawn'
        Account.debit(self,amount)

def show_accounts(acc):
    print(acc.accno,acc.balance)
    print(acc.__class__)
    print(isinstance(acc,Account))
    print(isinstance(acc,CreditAccount))


acc1 = Account(1000)
acc1.debit(30)
acc2 = CreditAccount(300,100)
acc2.credit(50)
acc2.debit(500)
for a in (acc1,acc2): show_accounts(a)
print(acc2.credit_limit)
