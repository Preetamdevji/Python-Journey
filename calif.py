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
elif opr == "-":
    print(num1 - num2)
elif opr == "/":
    print(num1 / num2)
elif opr == "*":
    print(num1 * num2)
else:
    print("invalid operation")

