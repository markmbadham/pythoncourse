'''
Created on 18 Aug 2017

@author: mark
'''
import sqlite3 as db
import logging as log

log.basicConfig()

class UserDB(object):
    
    def __init__(self):
        self.con = db.connect('userdb.sqlite')
        self.cur = self.con.cursor()
    
    def query(self, sql, *args):
        try:
            if args:
                self.cur.execute(sql,args)
            else:
                self.cur.execute(sql)
        except Exception as e:
            log.exception(e,'in query ',sql )
            
    def setup(self):
        sql = '''
        CREATE TABLE users(
        id INT PRIMARY KEY,
        username VARCHAR(64),
        password VARCHAR(64))'''
        
        self.query(sql)
    
    def addUser(self,id,username,password):
        sql = '''
        INSERT into users
        VALUES (?,?,?)'''
        self.query(sql,id,username,password)
        self.con.commit()
        
    def showUsers(self):
        sql = "SELECT * FROM users"
        self.query(sql)
        return self.cur.fetchall()
        
if __name__ == '__main__':
    users = UserDB()
    #users.setup()
    #users.addUser(1,'fred','hello')
    print(users.showUsers())    