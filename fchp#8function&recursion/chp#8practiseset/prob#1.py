user1 = int(input("enter the first no: \n"))
user2 = int(input("enter the second no: \n"))
user3 = int(input("enter the third no: \n"))

def greatest(num1 , num2 , num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
                return num2
        else:
             return num3
max = greatest(user1, user2, user3)
print("this is your greatest value" + " " + str(max))

max = greatest(user1, user2, user3)
print("this is your maximum value" + " " + str(max))
        
     
    