class Accounts(object):
    accounts = 0
    def __init__(self, balance=0):
        self.balance = balance
        Accounts.accounts += 1
        self.accno = Accounts.accounts
    
    def debit(self, amount):
        self.balance -=amount

    def credit(self, amount):
        self.balance +=amount

    def get_balance(self):
        return self.balance

class CreditAccounts(Accounts):
    def __init__(self, balance=0, credit_limit = 0): 
        Accounts.__init__(self, balance)
        self.credit_limit = credit_limit

    def debit(self, amount):
        assert self.balance + self.credit_limit > amount, 'Insufficient funds' 
        Accounts.debit(self, amount)

def test_accounts(o):
    print(o.__class__)
    print(isinstance(o,Accounts))
    print('accno',o.accno,'balance',o.get_balance())
    o.debit(1100)
    print('balance',o.get_balance())
    o.credit(300)
    print('balance',o.get_balance())


if __name__ == '__main__':
   o = Accounts() 
   test_accounts(o)
   o2 = CreditAccounts(1000) 
   test_accounts(o2)
   print(o2.credit_limit)

