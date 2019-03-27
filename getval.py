FILENAME = 'config.text'
def getval1(key):
    with open(FILENAME) as f:
        for line in f:
            if line.startswith(key):
                return line.split('=')[1].strip()


def getval2(key):
    f = open(FILENAME)
    lines = f.readlines()
    return  filter(lambda line:line.startswith(key), lines)[0].split('=')[1].strip()
 
def getval3(key):
    f = open(FILENAME)
    while True:
        line = f.readline(1024)
        if not line: break
        item, val = line.split('=')
        if item.strip() == key:
            return val.strip()


def getval4(key):
    f = open(FILENAME)
    while True:
        line = f.readline(1024)
        if not line: break
        pos = line.index('=')
        if key in line[:pos]:
            return line[pos+1:].strip()


def regexgetval1(key):
    import re
    f = open(FILENAME)
    for line in f:
        match = re.search(r'^\s*'+key+r'\s*=\s*(\w+)$', line)
        if match:
            return match.group(1)

def regexgetval2(key):
    import re
    content = open(FILENAME).read()
    match = re.search(r'^\s*'+key+r'\s*=\s*(\w+)$', content,re.M)
    if match:
        return match.group(1)
