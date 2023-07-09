# Write a program to check if a given year is a leap year.

user = int(input("Enter the year:"))

def check(num):
    if (num % 4 == 0):
        return "This is a leap year"
    else:
        return "This is not a leap year"
    
result = check(user)
print(result)