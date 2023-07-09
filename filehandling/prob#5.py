words = ['Dorothy','donkey','staring']

file_path = 'sampel.txt'

with open(file_path, 'r') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$$^^@@^!!")
with open(file_path, 'w') as f:
    f.write(content)