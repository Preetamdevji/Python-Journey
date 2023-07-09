path = 'replace.txt'

with open(path) as f:
    wipe = f.read()

with open(path, 'w') as f:
    wipe = f.write("")