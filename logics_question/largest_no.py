# Write a program to find the largest among three numbers.

user_1 = int(input("Enter the first number:"))
user_2 = int(input("Enter the second number:"))
user_3 = int(input("Enter the third number:"))

def check(first, second, third):
    if (first > third):
        if (first > second):
            return "First is the Largest number"
    elif (second > third):
        if (second > first):
            return "Second is the Largest number"
    else:
        return "Third is the Largest number"
    
result = check(user_1, user_2, user_3)
print(result)
    

       
        


