fileo = open('config.text','r')

for line in fileo:
    if line.startswith("port"):
        print(line.split('=')[1].strip())
        
fileo.seek(0)
lines = fileo.readlines()
print(filter(lambda x: x.startswith("port"), lines).__next__().split('=')[1].strip())


fileo.seek(0)
for line in fileo:
    key, val = line.split('=')
    if key.strip() == "port": print(val.strip())
