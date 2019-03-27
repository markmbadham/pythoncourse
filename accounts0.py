#!/usr/bin/env python3
class Accounts(object):
    accounts = 0
    types = ('A','L','I','E','OE')

    def __init__(self, balance = 0, atype = 'A'):
        self._balance = balance 
        self._type = atype

    def debit(self, amount):
        #self._balance += (amount if self._type in ('A','E') else -amount)
        if self._type == 'A' or self._type == 'E':
            self._balance += amount
        else:
            self._balance -= amount

    def credit(self,amount):
        self.debit(-amount)

    def get_balance(self):
        return self._balance

    def test_accounts(self):
        print(self)

class CreditAccounts(Accounts):
    def __init__(self, balance=0, atype='A', credit_limit=0 ):
        self.credit_limit = credit_limit
        Accounts.__init__(self,balance,atype)

    def debit(self, amount):
        if self._type in ('A','E'): value = -amount
        else: value = amount
        print(value,self._balance)
        if  self._balance + self.credit_limit > value:
            Accounts.debit(self, amount)
        else: 
            raise ValueError('insufficient funds') 

if __name__ == "__main__":
    o = CreditAccounts(100, credit_limit=100);
    print(o.get_balance())
    print(o.credit_limit)
    o.debit(50)
    o.credit(300)
    print(o.get_balance())
    print(isinstance(o,Accounts))
    print(isinstance(o,CreditAccounts))

