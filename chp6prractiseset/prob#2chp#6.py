sub_1 = int(input("enter your marks: \n"))
sub_2 = int(input("enter your marks: \n"))
sub_3 = int(input("enter your marks: \n"))

if (sub_1 < 33 or sub_2 < 33 or sub_3 <33):
    print("you are fail because of your marks")

elif (sub_1+sub_2+sub_3)/3 < 40:
    print("you are fail because of your percentage") 

else: 
    print("you are pass")
