'''
Created on 16 Aug 2017

@author: mark
'''
class Account(object):
    accounts = 0
    
    def __init__(self, balance = 0):
        self.balance = balance
    
    def debit(self, amount):
        self.balance -= amount
        
    def credit(self, amount):
        self.balance += amount
    
    def get_balance(self):
        return self.balance

class CreditAccount(Account):
    
    def __init__(self, balance=0, credit_limit=0):
        super().__init__(balance)
        self.credit_limit = credit_limit
    
    def debit(self, amount):
        assert amount < self.balance + self.credit_limit, "account overdrawn"
        super().debit(self, amount)

        
if __name__ == '__main__':
    current = Account()
    credit  = CreditAccount(balance=20)
    print(credit.__class__)
    print(isinstance(credit,Account))
    print(Account.accounts)
    current.credit(100)
    current.debit(10)
    credit.debit(50)
    #Account.debit(current,10)
    print(current.get_balance(), credit.balance)