# Write a program to reverse a string without using any built-in functions.

user = input("Enter the string:")

def reverse(str_rev):
    reversed_str = ""
    for i in range(len(str_rev)-1,-1,-1):
        reversed_str += str_rev[i]
    return reversed_str

reversed_string = reverse(user)
print("The reversed string is:", reversed_string)

# user = input("Enter the string:")

# def reverse(str_rev):
#     reverse_string = ""
#     for i in range(len(str_rev)-1, -1, -1):
#         reverse_string += str_rev[i]
#         return "The string is reverse" + " " + reverse_string
#     return "your string is not reverse"
    
# res = reverse(user)
# print(res)      
