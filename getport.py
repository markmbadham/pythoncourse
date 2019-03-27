FILENAME = 'config.text'
def get_port(filename=FILENAME):
    for line in open(filename):
        if line.startswith('port'):
            return line.split('=')[1].strip()

print get_port()

def get_config(filename=FILENAME):
    config = {}
    for line in open(filename):
        key, val = line.split('=')
        config[key.strip()] = val.strip()
    return config

print get_config()
