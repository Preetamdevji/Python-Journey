my_dict = {"name" : "Preetam", "age" : 26,"dollar" : "30.59$ i have","rupees" : 10000000000.555,"bollen" : True,
           'vegetables': {'carrot': 4, 'spinach': 5, 'broccoli': 6, 8 : 9 }}

# print(list(my_dict))

# print(my_dict.values())
#  python dictionary method

# print(my_dict.clear())
# print(my_dict.copy())
# print(my_dict.fromkeys("name", "love"))
# update_dict = {"coding" : "lover", "name" : "Python"}
# my_dict.update(update_dict)
# print(my_dict)




print(my_dict.get("name")) 
print(my_dict["name"])

# difference between get method and list

print(my_dict.get("name2"))    #its return none
print(my_dict["name2"])        #throw error it is not present in dict