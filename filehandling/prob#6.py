file_paths = 'G:\python\log.txt'

with open(file_paths,'rt') as f:
    content = f.read().lower()

if 'python' in content:
    print("yes")
else:
    print("no")