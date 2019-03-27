for i in updown(5):print i
d = {"name":"fred",
     "surname" : "basset",
     "age" : 10}
d["name"]
d["surname"]
d["age"]
d
help(d)
d["name"]
d.get("name")
d["arb"]
d.get("arb")
d.get("arb","none")
d["test"] = "testing"
d
d["name"] = "testing"
d
l = [d]
l[0]['age']
l[1] = {}
l += {}
l[1]["name"] = 'a'
l
l += {}
l
l.append({})
l
l += [{}]
l
l[1]["name"] = 'a'
l[2]["name"] = 'b'
l[0]['friends'] = []
l[0]['friends'].append("a")
l[0]['friends'].append("b")
l[0]['friends']
d.keys()
d.items()
d.pop('friends')
d
d.popitem()
d.popitem()
d.popitem()
d.popitem()
d.popitem()
d
d = {"name":"fred",
     "surname" : "basset",
     "age" : 10}
for e in d: print e
d.values()
for e in d: print e, d[e]
for (key,val) in d.items(): print key, val
l
{} in l
"fred" in d
"name" in d
"fred" in d.values()
"name" in d.keys()
d["friends"] = ['a','b','c']
c in d["friends"]
'c' in d["friends"]
if type(x) in (dict,set,list,tuple)
if type(d) in (dict,set,list,tuple)
if type(d) in (dict,set,list,tuple): print "yes"
if type(l) in (dict,set,list,tuple): print "yes"
from accounts import Account
Account.x
Account.x =1
Account.x 
Account.accno
Account.tye
Account.type
Account.type = "LIABILITY"
Account.type
Account.__doc__
s = "test"
s1 = "hello"
s.upper()
s1.upper()
str.upper()
check = Account()
check.x
check.type
check.balance=100
Account.balance
card = Account
card = Account()
card.x
card.balance
Account.__dict__
Account.__dict__['x']
card.__dict__
check
check.__dict__
card.__dict__.get('balance',0)
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
from accounts import Account
check = Account()
card = Account()
check.balance = 100
check.debit(5)
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import cvs
import csv
reader = csv.reader(open('students.csv'),delimiter='\t')
reader.next()
for row in reader: print row
dict([('name','fred'),('surname','basset'),('age','10')])
keys = ['name','surname','age']
row = ['fred','basset','10']
zip(keys,row)
reader = csv.reader(open('students.csv'),delimiter='\t')
keys = reader.next()
list_of_dicts = []
for row in reader:
    list_of_dicts.append(dict(zip(keys,row)))
    
list_of_dicts
list_of_dicts[3]
list_of_dicts[3]['Company']
1/0
try:
    1/0
except ZeroDivisionError:
    print "can't devide by zero"
    
try:
    1/0
    l[0] =1
except ZeroDivisionError:
    print "can't devide by zero
try:
    l[0] =1
    1/0
except:
    print "can't devide by zero"
try:
    l[0] =1
    1/0
except ZeroDivisionError:
    print "can't devide by zero"
except NameError:
    print "l does not exist"
import Traceback as tb
import traceback as tb
tb.print_stack()
tb.format_exc(limit)
tb.format_exc()
raise NameError,"broken"
int('a')
import socket
sock = socket.socket()
sock.connect(('10.0.4.1',80))
sock.send("GET / HTTP/1.0\n\n\n")
sock.recv(4096)
sock.send("GET / HTTP/1.0\n\n\n")
sock.connect(('10.0.4.1',80))
sock.close()
sock.connect(('10.0.4.1',80))
sock = socket.socket()
sock.connect(('10.0.4.1',80))
sock.send("GET / HTTP/1.0\n\n\n")
sock.recv(4096)
sock.close()
sock = socket.socket()
sock.connect(('10.0.4.1',25))
sock.send("EHLO 10.0.4.33")
sock.recv(4096)
sock.recv(4096)
lsock = socket.socket()
lsock.bind('127.0.0.1',10000)
lsock.bind(('127.0.0.1',10000))
lsock.listen(5)
(bsock,add) = lsock.accept()
bsock.send("hello\r\n")
bsock.recv(4096)
bsock.close()
lsock.close()
import logging as log
help(log)
d = {'name':'server','time':'13:04','message':'testing112'}
print '%(time)s - %(name)s - %(message)s' % d
log.basicConfig(filename='test.log',level=log.DEBUG)
log.debug('test1')
open('test.log').read()
log.BASIC_FORMAT
log.basicConfig(filename='test.log',level=log.DEBUG,format='%(asctime)s'+log.BASIC_FORMAT)
log.debug('test2')
open('test.log').read()
help(log)
log.BASIC_FORMAT
log.basicConfig(filename='test.log',level=log.DEBUG,format='%(asctime)s'+log.BASIC_FORMAT)
open('test.log').read()
print open('test.log').read()
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import logging as log
log.basicConfig(filename='test.log',level=log.DEBUG,format='%(asctime)s'+log.BASIC_FORMAT)
log.warn('test3')
print open('test.log').read()
