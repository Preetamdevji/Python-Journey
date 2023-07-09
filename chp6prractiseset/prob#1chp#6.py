user_1 = int(input("enter your number: \n"))
user_2 = int(input("enter your number: \n"))
user_3 = int(input("enter your number: \n"))
user_4 = int(input("enter your number: \n"))

if  (user_1 > user_4):
  f1 = user_1

else:
  f1 = user_4

if (user_2 > user_3):
    f2 =  user_2

else:
    f2 =  user_3

if (f1 > f2):
   print(str(f1) + " " + "is greatest")

else:
   print(str(f2) + "is greatest")   