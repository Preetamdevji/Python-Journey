a = "Good Night dear"
b = input("enter your user name: \n")
print(b,a)


name = "Ritika"
join_date = "1/April/2023"

letter = input('''Dear {}
                you are selected 
                    {}
                        if you are any issue contact our support department.
                            Regards Preetam devji
                                Thanks you dear.'''.format(name, join_date))

print(letter)


detect = "This is Preetam and  his learnig python"
doublspace = detect.find("  ")
print(doublspace)

detect = "This is Preetam and  his learnig python"
singlespace = detect.replace("  " , " ")
print(singlespace)

escape = "\"This is Preetam and he is find love\""
print(escape)




