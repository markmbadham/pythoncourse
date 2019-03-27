from accounts02 import Account

class CreditAccount(Account):
    def __init__(self, openingbalance =0, creditlimit = 0):
        Account.__init__(self, openingbalance) 
        self.creditlimit = creditlimit

    def debit(self, amount):
        assert amount < self.balance + self.creditlimit, 'account overdrawn'
        Account.debit(self,amount)

if __name__ == '__main__':
    cc = CreditAccount(100, 50)
    print('Accno: %s' % cc.accno)
    print('balance: %s' % cc.balance)
    cc.debit(50)
    print('balance: %s' % cc.balance)
    print(isinstance(cc,Account))
    print(isinstance(cc,CreditAccount))
    print(cc.creditlimit)
    cc.debit(200)
