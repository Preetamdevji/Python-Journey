class Vehicle:
    def __init__(self,milege,cost):
        self.milege = milege
        self.cost = cost

    def show_vehicle_details(self):
        print("The milege is:",self.milege)
        print("The cost is:",self.cost)
        print("This is my vehicle")

v1 = Vehicle(50,"20lac")
v1.show_vehicle_details()

class Car(Vehicle):
    def show_car_details(self):
        print("This is my car")

c1 = Car(40, "30lac")
c1.show_vehicle_details()
c1.show_car_details()