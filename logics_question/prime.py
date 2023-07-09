# Write a program to find the prime numbers.

user = int(input("Enter the value: \n"))

def check(num):
    for i in range(1 , num):
        if num % 2 ==  0:
            return "This is not Prime number"
        else:
            return "This is Prime number"
        
res = check(user)
print(res)
