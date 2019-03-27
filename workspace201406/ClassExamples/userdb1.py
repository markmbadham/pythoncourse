'''
Created on 18 Jul 2014

@author: mark
'''
import sqlite3 as db

class UserDB(object):
    def __init__(self):
        self.con = db.connect('mydb.db')
        self.cur = self.con.cursor()

    def setup(self):
        sql = '''
        CREATE TABLE users(
        id int PRIMARY KEY,
        name VARCHAR(64),
        password VARCHAR(64))
        '''
        self.cur.execute(sql)
        self.con.commit()

    def add_user(self,rid,name,password):
        sql = '''INSERT INTO users 
            VALUES(%s,'%s','%s')''' % (rid,name,password)
        self.cur.execute(sql)
        self.con.commit()
    
    def show_table(self,table='users'):
        sql = "SELECT * FROM " + table
        self.cur.execute(sql)
        print map(lambda x:x[0],self.cur.description)
        for row in self.cur:
            print '\t'.join(map(str,row))    
        
if __name__ == '__main__':
    u = UserDB()
    u.show_table()
    #u.add_user(4, 'Harry', 'qqqqq')
    #u.show_table()