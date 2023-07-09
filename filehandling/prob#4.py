with open('replace.txt', 'r') as f:
    content = f.read()

content = content.replace("donkey", "$$^&&^@@")
with open('replace.txt', 'w') as f:
    f.write(content)