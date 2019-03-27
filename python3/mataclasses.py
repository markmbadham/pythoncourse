#!/usr/bin/env python3
class CustomMetaclass(type):
    def __init__(cls, name, bases, dct):
        print("Creating class %s using CustomMetaclass" % name)
        print("dict: %s " % dct.__repr__())
        super(CustomMetaclass, cls).__init__(name, bases, dct)

class BaseClass(object,metaclass=CustomMetaclass):
    #__metaclass__ = CustomMetaclass for python2
    def test(self):pass

class Subclass1(BaseClass):
    pass
