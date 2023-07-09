user = int(input("enter the number: \n"))

def multiplication(user):
    result = ""
    for i in range(1, 13):
        result += str(user) + " x " + str(i) + " = " + str(user * i) + "\n"
    return result
    
test = multiplication(user)
print(test)






