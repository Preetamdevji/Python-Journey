user = int(input("Enter the celsius: \n"))


def farh(cel):
    return (cel * (9/5)) + 32

celsius = farh(user)
print("This is your fahrenheit value" + " " + str(celsius))