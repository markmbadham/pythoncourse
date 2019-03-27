'''
Created on 10 Jun 2014

@author: mark
'''

class Account(object):
    '''
    classdocs
    '''
    last_accno = 0
    types = ("ASSET","LIABILITY","EQUITY","INCOME","EXPENCE")
    _perm_accounts = types[:3]
    _credit_accounts = types[1:4]
    _debit_accounts = types[0] +types[4]
    
    def __init__(self,balance=0):
        self.balance = balance
        Account.last_accno += 1
        self.accno  = Account.last_accno
        self.type = Account.types[0]
        
    def debit(self,amount):
        self.balance += amount if self.type in Account._debit_accounts else -amount
        
    def credit(self,amount):
        self.balance += amount if self.type in Account._credit_accounts else -amount

class CreditAccount(Account):
    def __init__(self,credit_limmit=0,balance=0):
        Account.__init__(self,balance)
        self.credit_limmit = credit_limmit
    
    def credit(self,amount):
        assert self.balance + self.ceditlimmit > amount, "not enough funds"
        Account.credit(self,amount)
                
if __name__ == "__main__":
    check = Account()
    card = CreditAccount()
    print isinstance(check,Account)
    card.type = "LIABILITY"
    print card.balance
    check.balance = 100
    check.debit(5)
    print check.balance
    card.debit(50)
    print card.balance
    card.debit(10) #Account.debit(card,10)
    print card.balance
    print Account.__dict__