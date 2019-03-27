class Accounts(object):
    accs = 0
    def __init__(self, balance=0):
        self.balance = 0

    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.debit(-amount) 

    def get_accs(self):
        print(self.__dict__)
        return Accounts.accs

class CreditAccounts(Accounts): 
    def __init__(self, balance = 0):
        Accounts.__init__(self)
        self.creditlimit = 0

current = Accounts()
print(current.balance)
current.credit(10)
print(current.balance)

