path = 'log.txt'
content = True
i = 1
li = ['python', 'c++']
with open(path, 'r') as f:
   while content:
      content = f.readline()

      if any(word in content.lower() for word in li):
         print(content)
         print(f"The is present on line {i}" + " " + str(content))
      
      i += 1

