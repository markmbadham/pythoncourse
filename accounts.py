class Accounts(object):
     total_accounts = 0
     def __init__(self, balance=0):
         self.balance= balance
         Accounts.total_accounts+=1

     def credit(self, amount):
         self.balance += amount

     def debit(self, amount):
         self.balance -= amount

class CreditAccounts(Accounts):
     def __init__(self, *args, **kwargs):
         if 'credit_limmit' in kwargs:
             self.credit_limmit = kwargs.pop('credit_limmit')
         else: self.credit_limmit = 0
         Accounts.__init__(self, *args, **kwargs)
     
     def debit(self, amount):
         assert amount < self.credit_limmit + self.balance, "acount overdrawn"
         Account.debit(self,amount)

if __name__ == "__main__":
    current = Accounts()
    credi_card = CreditAccounts()
    print isinstance(credi_card,Accounts)
    print credi_card.__class__
    #current.balance = 0
    current.credit(500)
    Accounts.credit(current,500)
    print current.balance
