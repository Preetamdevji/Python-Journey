class Mobile:
    def __init__(self):
        self.model = "Real me X"
        self.color = "Navy Blue"
        

    def get_info(self):
        return self.model
    
    def get_info_1(self):
        return self.color


m1 = Mobile()
res_1 = m1.get_info()
res_2 = m1.get_info_1()
print(res_1,res_2)