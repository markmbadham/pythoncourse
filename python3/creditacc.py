from accounts import Accounts
class CreditAccount(Accounts):
    def __init__(self, credit_limit=0):
	Accounts.__init__(self)
        self.credit_limit=credit_limit 

    def debit(self, amount):
       if self.balance + self.credit_limit > amount:
           Accounts.debit(self,amount)
       else: raise ValueError("Insufficient funds")

if __name__ == "__main__":
    visa = CreditAccount(100)
    print(visa.balance)
    visa.credit(400)
    print(visa.balance)
    print(isinstance(visa,CreditAccount))
    visa.credit_limit += 100
    

