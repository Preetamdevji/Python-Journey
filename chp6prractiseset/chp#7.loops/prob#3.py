num = int(input("Enter the number \n"))

Prime = True

for i in range(2 , num):
    if (num%i == 0):
        Prime = False
        break
    if Prime:
            print("This is prime number")
    else:
            print("This is not prime number")