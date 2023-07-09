user = int(input("Enter the Number"))

def calculate(num):
    factorial = 1

    if num < 0:
        return "The factorial does not exist for negative integers"
    elif num == 0:
        return "The factorial of zero is 1"
    else:
        for i in range(1, num + 1):
            factorial *= i

        return "The factorial of " + str(num) + " is " + str(factorial)

result = calculate(user)
print(result)
