# Write a program to check if a string is a palindrome

user = input("Enter the Word: \n")

def checkpalindrone(word):
    rev = "" . join(reversed(word))     #take null string then concadinate with join  method and the join with predifined reversed function. 

    # now we check its equal or not
    if word == rev:
        return True
    return False

# Then we call the function

res = checkpalindrone(user)
 
if (res):
    print("Yes, it is a palindrome.")
else:
    print("No, it is a palindrome.")