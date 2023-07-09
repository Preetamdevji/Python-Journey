# Write a program to find the prime numbers between a given range.

# Take Input with user

user_1 = int(input("Enter the lower  value: \n"))
user_2 = int(input("Enter the upper value: \n"))

# start def func 

def check(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# find prime no is in given range

def findprime(num1, num2):
    primes = []
    for num in range(num1, num2 + 1):
        if check(num):
            primes.append(num)
            return primes

       
res = findprime(user_1, user_2)
print("Prime numbers between", user_1, "and", user_2, "are:")
print(res)

           








