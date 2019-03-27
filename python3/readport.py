def readval(key):
    f = open('config.text')
    for line in f:
        if line.startswith(key):
            return line.split('=')[1].strip()


import re
def readvalre(key):
    f = open('config.text')
    for line in f:
        match = re.search('^%s\\s*=\\s*(.+?)\\s*$' % key, line)
        if match : return (match.group(1))

def readvalre2(key):
    return re.search('^%s\\s*=\\s*(.+?)\\s*$' %key, open('config.text').read(),re.M+re.I).group(1)
            


print(readvalre('port'))
print(readvalre2('host'))
