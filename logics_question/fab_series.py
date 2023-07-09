# Write a program to find the Fibonacci series up to a given number.


def fib(n):
    fib_series = []
    a = 0
    b = 1

    for _ in range(n):
        fib_series.append(a)

        a , b , b = a + b

    return fib_series

user = int(input("Enter the number of Fibonacci terms: "))

result = fib(user)
print("Fibonacci Series:" + " " + str(result))












  
        
    
    
