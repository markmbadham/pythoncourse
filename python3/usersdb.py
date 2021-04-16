import sqlite3 as db
import logging as log

log.basicConfig(
    format = '%(actime):' + log.BASIC_FORMAT,
    filename = 'userdb.log',
    level = log.DEBUG
)

conn = db.connect('users.db')
cur = conn.cursor()

def query(sql, *params):
    log.debug("Execute query: %s" % sql)
    try:
        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)

    except db.DatabaseError as e:
        log.exception("Error in %s" % sql)
    else: print("query succeeded")

def setup():
    sql = '''CREATE TABLE users(
             id INT PRIMARY KEY,
             username VARCHAR(64),
             password VARCHAR(64))'''
    query(sql)

def add_user(userid, username, password):
    sql = '''INSERT INTO users
             VALUES (?,?,?)'''
    query(sql, userid, username, password)
    conn.commit()

def show_users():
    sql = 'SELECT * FROM users'
    query(sql)
    for row in cur:
        print('\t'.join(map(str,row)))

show_users()

conn.close()