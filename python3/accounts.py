class Accounts(object):
     total_accounts = 0
     def __init__(self):
         self._balance=0
         Accounts.total_accounts+=1

     def credit(self, amount):
         self.__dict__['_balance'] += amount

     def debit(self, amount):
         self.__dict__['_balance'] -= amount

     def __del__():
        pass

     def __delattr__(self,name):
        if name.startswith("_"):
            raise Exception("cannot delete private attribute")
     
     def __getattribute__(self,name):
        if name.startswith("_"):
            raise Exception("cannot get private attribute")
        else: return self.__dict__['name']

if __name__ == "__main__":
    current = Accounts()
#    del(current._balance)
    credi_card = Accounts()
    #current.balance = 0
    current.credit(500)
    Accounts.credit(current,500)
    #print(current._balance)
