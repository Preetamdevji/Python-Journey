class Calculator:
     def __init__(self,number):
          self.number = number

     def square(self):
        print(f"The square {self.number} of {self.number **2}")
     
     def square_root(self):
         print(f"The square root {self.number} of {self.number ** 0.5}")

        
     def cube(self):
        print(f"The cube {self.number} of {self.number **3}")

     @staticmethod
     def greet():
         print("Hello")
c1 = Calculator(2)
c1.square()
c1.square_root()
c1.cube()
c1.greet()