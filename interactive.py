#!/usr/bin/env python
'''
name = raw_input("Enter your name: ")
surname = raw_input("Enter your surname: ")
print "Hello " + name + " " + surname

a = raw_input("first number: ")
b = raw_input("second number: ")
print int(a) + int(b)
'''
principle_str = raw_input("Principle: ")
rate_str = raw_input("Rate: ")
period_str = raw_input("Period: ")

principle = float(principle_str)
rate = float(rate_str)
period = int(period_str)
print "Answer = %6.2f:"  %  (principle * (1 + rate) ** period)
