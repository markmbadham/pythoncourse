class Accounts(object):
    accounts = 0
    def __init__(self, balance = 0):
        self.balance = balance
        Accounts.accounts += 1
        self.accno = Accounts.accounts

    def debit(self, amount):
        self.balance -=amount

    def credit(self, amount):
        self.balance +=amount

class CreditAccounts(Accounts): 
    def __init__(self, balance=0, credit_limit=0):
        Accounts.__init__(self, balance)
        self.credit_limit = credit_limit

    def debit(self, amount):
        assert amount < self.balance + self.credit_limit, 'account ovwrdrawn'
        Accounts.debit(self, amount)

def test_account(*accs):
    for acc in accs:
        acc.debit(50)
        print acc.accno,'balance', acc.balance
        print acc.__class__
        print 'Accounts ',isinstance(acc,Accounts)
        print  'CreditAccounts ', isinstance(acc,CreditAccounts)


if __name__ == '__main__':
    acc1 = Accounts(100)
    acc2 = CreditAccounts(200)
    acc3 = Accounts()
    test_account(acc1,acc2,acc3)
    print acc2.credit_limit
