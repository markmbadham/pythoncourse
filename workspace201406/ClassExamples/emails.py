'''
Created on 10 Jun 2014

@author: mark
'''

class EmailUser(object):
    '''
    classdocs
    '''

    def __init__(self, email_address):
        '''
        Constructor
        '''
        self.email_address = email_address
    
    def email(self,to,subject,message):
        to_address = to.email_address
        msg = "FROM: " + self.email_address + "\n TO: " + to_address+ "DATE:\nSUBJECT:" + subject
        