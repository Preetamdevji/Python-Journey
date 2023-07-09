class Vehicle:
    def __init__(self,milege,cost):
        self.milege = milege
        self.cost = cost

    def show_vehicle_details(self):
        print("The milege of vehicle is:",self.milege)
        print("The cost of vehicle is:", self.cost)
    
class Car(Vehicle):
    def __init__(self,milege,cost,color,horsepower):
        super(). __init__(milege,cost)
        self.color = color
        self.horsepower = horsepower
        print("The color of Car is:", self.color)
        print("The Vehicle HorsePower is:",self.horsepower)

c1 = Car(50, "25lac", "White","2000HP")
c1.show_vehicle_details()



