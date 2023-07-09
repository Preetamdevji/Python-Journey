print('''
    +:Addition
    -sub
    /div
    *multiple
''')

num1 = eval(input("enter the first value: "))
opr = input("operation (+,-,/,*)")
num2 = eval(input("Enter the second value: "))


if opr == "+":
    print(num1 + num2)
if opr == "-":
    print(num1 - num2)
if opr == "/":
    print(num1 / num2)
if opr == "*":
    print(num1 * num2)

if opr != "+" and opr != "-" and opr != "/" and opr != "*":
    print("invalid opr...")
