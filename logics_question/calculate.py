# Write a program to calculate the sum of digits in a number

user = int(input("Enter the value: \n"))

def calculate(num):
    total = 0
    while num != 0:
        digit = num % 10  # Extract the last digit
        total += digit   # Add the digit to the total
        num //= 10       # Remove the last digit from the number
    return total

res = calculate(user)
print(res)

    

