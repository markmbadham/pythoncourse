'''
Created on 13 Jun 2014

@author: mark
'''
import sqlite3 as db

class UserDB(object):
    def __init__(self):
        self.con = db.connect('userdb.db')
        self.cur = self.con.cursor()

    def setup(self):
        sql = '''
           CREATE TABLE users(
               id INT PRIMARY KEY,
               name VARCHAR(64),
               password VARCHAR(64))
               '''
               
        self.cur.execute(sql)

    def add_user(self,id,name,password):
        sql = "INSERT INTO users VALUES(%s,'%s','%s')" % (id,name,password)
        self.cur.execute(sql)
        self.con.commit()
    
    def showtable(self,table='users'):
        sql = "SELECT * FROM %s" % table
        self.cur.execute(sql)
        out = ''
        for data in self.cur.description:
            out += data[0] + '\t'
        out += '\n'
        for row in self.cur: 
            out += '\t'.join(map(str,row)) + '\n'
        return out
    
    def getfields(self,table='users'):
        sql = "SELECT * FROM %s limit 1" % table
        self.cur.execute(sql)
        return map(lambda x:x[0],self.cur.description)

    
    def auth(self,user,password):
        sql = "SELECT pass FROM users WHERE name = '%s'" % user
        self.cur.execute(sql)
        return password == self.cur.fetchone()[0]
    
    def auth2(self,user,password):
        sql = "SELECT pass FROM users WHERE name = '%s' and pass = '%s'" % (user,password)
        self.cur.execute(sql)
        return self.cur.rowcount > 0

if __name__ == "__main__":
    userdb = UserDB()
    userdb.setup() # UserDB.setup(userdb)
    print userdb.showtable()
