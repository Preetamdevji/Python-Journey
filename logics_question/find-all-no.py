# Write a program to find the sum of all numbers between 1 and a given number.

user = int(input("Enter the number: \n"))

def cal_sum(num):
    total = 0
    for i in range(1 , num + 1):
        total += i
    return "The sum of all numbers" +" " + str(total) 
     
res = cal_sum(user)
print(res)

