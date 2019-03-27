email = input('Enter an email: ')
tld_pos = email.rfind('.')
tld = email[tld_pos+1:]
print(tld)