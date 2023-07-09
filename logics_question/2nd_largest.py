# Write a program to find the second largest number in a list.

l1 = [88,99,10,6,3,5,35,14,5,5,45,528,412654,45,588614]

def check(num):
    num.sort()
    return num[-2]




res = check(l1)
print(res)