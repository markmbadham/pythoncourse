Programming Python
==================

Mark Badham
-----------

Python Software:
----------------

[\\\\vault\\software\\python](smb://vault/software/python)
----------------------------------------------------------

Start 09:00
-----------

Tea 10:30-45
------------

Lunch 12:00-45
--------------

Tea 14:30-45
------------

What is Python {#what-is-python style="page-break-before:always; "}
==============

-   Standard vs Implementation
-   Compiled vs Interpreted
-   Open Source
-   BDFL: Guido van Rossam
-   Version 3.x vs 2.x

Python Philosophy {#python-philosophy style="page-break-before:always; "}
=================

-   Explicit rather than implicit
-   One obvious way to do it
-   No surprises (consistency)
-   Batteries included

Using the Python Shell {#using-the-python-shell style="page-break-before:always; "}
======================

`
\$ python
---------

Python 2.7.9 (default, Apr 2 2015, 15:33:21)
--------------------------------------------

\[GCC 4.9.2\] on linux2
-----------------------

Type "help", "copyright", "credits" or "license" for more information.
----------------------------------------------------------------------

&gt;&gt;&gt;
------------
`
Python Syntax {#python-syntax style="page-break-before:always; "}
=============

Case Sensitive

One statement per line

Statement can be an expression

Comment `\#`

No multi line comment use Docstring

-`   ''' … '''`

Extending a line {#extending-a-line style="page-break-before:always; "}
================

-   Backslash \\
-   Open ( \[ {
-   Or triple quoted string '''

Writing Programs {#writing-programs style="page-break-before:always; "}
================

Edit hello.py
`
-   \#!/usr/bin/env python
-   print('hello')
-   input()
`
Executing Programs {#executing-programs style="page-break-before:always; "}
==================

From windows explorer:

-   Double click on file

From idle:

-   press f5
-   Or choose run from the menu

From CMD:

-   Type: hello.py

Using Variables {#using-variables style="page-break-before:always; "}
===============

Naming rules
`
-   \^\[A-Za-z\_\]\[A-Za-z0-9\_\]\*\$
`
Style Guide

-   Variables lowercase
-   multi\_word\_vars
-   CONSTANTS
-   ClassNames

Builtin Types {#builtin-types style="page-break-before:always; "}
=============

Numeric

-   int, long (py2), float, complex

Sequences

-   str, list, tuple

Other Iterables

-   set, frozenset, dictionary, file

Structures

-   Functions, Classes, Modules

Integers {#integers style="page-break-before:always; "}
========
`
  i =10
  type(i)
  i = 0xFE
  type(i)
`
floats {#floats style="page-break-before:always; "}
======
`
  f = 2.0
  type(f)
  f = 3E2
  type(f)
`
Complex {#complex style="page-break-before:always; "}
=======
`
  3.0+54j
`
Sequences {#sequences style="page-break-before:always; "}
=========

Indexing
`
-   Seq\[0\] … Seq\[-1\]
`
Slicing

-   Seq\[start:end:step\]
-   Default start = 0
-   Default end = -1
-   Default step = 1

Sequence Functions Methods and Operators {#sequence-functions-methods-and-operators style="page-break-before:always; "}
========================================
`
-   len(Seq)
-   Seq.index()
-   Seq.count()
-   val in Seq
-   + \*
`
Strings {#strings style="page-break-before:always; "}
=======

Are Sequences

Delimited by quotes

-   Double quotes “”
-   Single quotes ''
-   Or triple quoted ''' ''' or '''''' ''''''

String Formatting {#string-formatting style="page-break-before:always; "}
=================
`
change = 5

print(“the change is %s cents” % change)

   the change is 5 cents

print(“the change is %d cents” % change)

   the change is 5 cents
`
Format width {#format-width style="page-break-before:always; "}
============
`
print(“the change is %05s cents” % change)

   the change is 5 cents

print(“the change is %05d cents” % change)

   the change is 00005 cents
`
Format float {#format-float style="page-break-before:always; "}
============
`
change = 5 + 2/3.0

   5.6666666666666666

print(“the change is %06.2f cents” % change)

   the change is 005.66 cents
`
String Methods {#string-methods style="page-break-before:always; "}
==============

Index / find

-   index(), find(), rindex(), rfind(), count()

Strip

-   strip(), rstrip(),strip()

Case

-   upper(), lower(), capitalize()

String Exercise {#string-exercise style="page-break-before:always; "}
===============

Given
`
   email = <fred@acme.com> or similar
`
Code

-   Use index() and slicing to display *fred*

String Answer {#string-answer style="page-break-before:always; "}
=============
`
email = '<fred@acme.com>'

atindex = email.index('@')

print(email\[:atindex\])
`
`
   fred
`
`
print(email\[:email.index('@')\])
`
`
   fred
`
Lists {#lists style="page-break-before:always; "}
=====

Delimiter \[\]

-   l1 = \[1,2,3,4\]
-   **print**(l1\[2\])
-   3

Lists are mutable

List Methods {#list-methods style="page-break-before:always; "}
============

Growing lists

-   append(), extend(), insert()

Shrinking lists

-   pop(), remove(), clear()

Sorting lists

-   sort(), reverse()

Dictionaries {#dictionaries style="page-break-before:always; "}
============

Delimiter {}

-   d1 = {'name':'fred', 'surname':'basset'}

print d\['name'\]

-   fred

Dictionary Methods operations {#dictionary-methods-operations style="page-break-before:always; "}
=============================

Overwrite or add new items

-   dict1\[key\] = value

Get item

-   dict1\[key\] or dict1.get('key'\[,default val\])

Delete item

-   del(dict1\[key\])

List keys values

-   keys(), values(), items()

Flow Control {#flow-control style="page-break-before:always; "}
============

IF

if condition:

-   statements

elif condition:

-   statements

else:

-   statements

Flow Control {#flow-control-1 style="page-break-before:always; "}
============

While

while condition:

-   statements
-   if … break
-   if … continue

else

-   statements

Flow Control {#flow-control-2 style="page-break-before:always; "}
============

For

for var in *iterable*:

-   statements
-   if … break
-   if … continue

else:

-   statements

Functions {#functions style="page-break-before:always; "}
=========

Definition

def function\_name():

-   statements

Calling Function

-   *function\_name()*

Function Return {#function-return style="page-break-before:always; "}
===============

-   Functions are not required to return
-   Return expression preferred to side affects

Parameters {#parameters style="page-break-before:always; "}
==========

def fn(arg1, arg2):

-   statements

fn(1,2)

-   calls function fn with arg1=1 and arg2=2

fn(arg2=1,arg1=2)

-   calls function fn with arg2=1 and arg1=2

Optional Arguments {#optional-arguments style="page-break-before:always; "}
==================

def fn(arg1, arg2=0):

-   statements
-   Default values make an argument optional
-   All mandatory arguments are defined before any optional arguments.

Variabe argument lists {#variabe-argument-lists style="page-break-before:always; "}
======================

def fn(\*args):

-   print(args)

fn(1,2,3**)**

-   (1,2,3)
-   **args** becomes a tuple

Key word args {#key-word-args style="page-break-before:always; "}
=============

def fn(\*\*kwargs):

-   print(kwargs)

fn(a='A',b='B')

-   {a:'A',b:'B'}
-   **kwargs** becomes a dictionary

lambda {#lambda style="page-break-before:always; "}
======

Inline anonymous function

lambda **arg1\[,...\]** : expression

-   arg1\[,...\] function argument list
-   expression is returned by the function
-   

Simple lambda functions {#simple-lambda-functions style="page-break-before:always; "}
=======================

Square

-   lambda x: x\*\*2

Even

-   lambda x: x%2==0

Map {#map style="page-break-before:always; "}
===

map( lambda x : x\*\*2, range(5))

-   0 1 4 9 16

Filter {#filter style="page-break-before:always; "}
======

filter( lambda x : x%2==0, range(5))

-   0 2 4

List Comprehension {#list-comprehension style="page-break-before:always; "}
==================

\[ x\*\*2 for x in range(5)\]

-   \[0, 2, 4, 9, 16\]
-   Actual list created

Generator expression {#generator-expression style="page-break-before:always; "}
====================

for i in (x\*\*2 for x in range(5))

-   print(i, end=None)
-   04816
-   Not an actual list
-   Iterable object i.e. has \_\_next\_\_()

Generator Functions {#generator-functions style="page-break-before:always; "}
===================

yield

-   Keyword always present in generator function
-   Function retuns a generator object
-   \_\_next\_\_()
-   Excutes up until **yield**
-   “break point” where execution temporarily stops and returns a value

Updown {#updown style="page-break-before:always; "}
======

def updown(n)**:**
------------------

for i in range(n): yield i
--------------------------

for i in range(n,0,-1): yield i
-------------------------------

for x in updown(5) : print(x, end='')
-------------------------------------

0123454321
----------

Modules {#modules style="page-break-before:always; "}
=======

-   Normal python file
-   Or pre-compiled C object, .dll .so
-   Found in sys.path

import {#import style="page-break-before:always; "}
======

import module

-   Creates a namespace
-   Named after module
-   Same as file name sans extension
-   Hence filename must be valid python identifier

Import invocation {#import-invocation style="page-break-before:always; "}
=================

-   import mod
-   import mod1, mod2
-   import mod1 as alias
-   from mod import attribute\[, ...\]
-   from mod import \*

Class {#class style="page-break-before:always; "}
=====

Allows custom objects

Contains

-   Class variables
-   Methods

Class Variable {#class-variable style="page-break-before:always; "}
==============

-   Normal variable
-   Class acts as a namespace

Methods {#methods style="page-break-before:always; "}
=======

-   Must accept *self*
-   Self represents the *instance object* the method was called from

Instance Vars {#instance-vars style="page-break-before:always; "}
=============

-   Variables contained in the *instance*
-   c1 = C()
-   c1.var
-   c1.\_\_dict\_\_\[‘var’\]

Constructor {#constructor style="page-break-before:always; "}
===========

\_\_init\_\_()

-   Intercepts the ClassName() call.
-   Often used to initialise instance variables

Inheritance {#inheritance style="page-break-before:always; "}
===========

Class definition

-   class ClassName(BaseClass\[,...\])
-   Attribute resolution delegation

Exceptions {#exceptions style="page-break-before:always; "}
==========

-   try: block
-   except \[ExceptionClass\]: block
-   else: block
-   finally: block

Raising Exceptions {#raising-exceptions style="page-break-before:always; "}
==================

-   raise ExceptionClass, message (py2)
-   raise ExceptionClass(message) (py3)
-   assert boolean\_expression, message

IO {#io style="page-break-before:always; "}
==

The os module

-   Import os
-   os.access, oss.listdir
-   os.path.isdir, isfile, os.path.abspath

Opening Files {#opening-files style="page-break-before:always; "}
=============

Open

-   open(‘filename’, ‘mode’)
-   Returns file object

Modes

-   ‘r’ read only (default)
-   ‘w’ write only
-   ‘+’ read and write (not recommended)

Reading Files {#reading-files style="page-break-before:always; "}
=============

-   for line in f: ...
-   f.readline(\[length\]) -&gt; str line
-   f.readlines(\[length\]) -&gt; list lines
-   f.read(\[length\]) -&gt; str content

Writing Files {#writing-files style="page-break-before:always; "}
=============

-   f = open(filename \[, ‘w’|’a’\])
-   f.write(str)
-   f.writelines(list)

 {#section-2 style="page-break-before:always; "}
