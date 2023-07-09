class Mobile:
    def __init__(self):
        self.model = "Real me X"
        self.color = "Navy Blue"
        

    def set_info(self):
        self.model = "Samsung Galaxy"
    
    def set_info_1(self):
        self.color = "JET BLACK"


m1 = Mobile()
#before
print(m1.model)
# after
m1.set_info()
print(m1.model)
# before
print(m1.color)
# after
m1.set_info_1()
print(m1.color)
